import binascii  # read pydoc .pcap file is a binary file , we need to convert HEX values to binary eventually
import os
from datetime import datetime, timedelta
import sys
import time
import copy
# read pydoc , we need this to perform full copy from variable to variable (works on lists , tuples , dictionaries)
import subprocess as sub
import random

port = 9600
PCAP_NAME = "pcap_file.pcap"
NUMBER_OF_PACKETS = 1000
RESOLUTION = 1  # time interval between packets in milliseconds
# SOURCE_IP = '10.20.20.20'
# read on map (maps function to str) maps output of random.int
SOURCE_IP = "172.172." + ".".join(map(str, (random.randint(0, 255) for _ in range(2))))
DEST_IP = '97.161.48.236'
RUN_TIME = 400  # sec
CALIB_TIME = 10  # this is required to control bandwidth
# Calibration is performed during initial 10 sec of runtime
mbps = 20
asset = '97.161.48.236'
sdcc = '10.20.4.49'

# Custom Foo Protocol Packet
# message =  ('01 01 00 08'   #Foo Base Header
#             '01 02 00 00'   #Foo Message (31 Bytes)
#             'D7 CD')        #Foo flags

message = '01'  # Base Header
# print "len message: ",len(message)


# Global header for pcap 2.4

# This is string
pcap_global_header = ('D4 C3 B2 A1'
                      '02 00'  # File format major revision (i.e. pcap <2>.4)
                      '04 00'  # File format minor revision (i.e. pcap 2.<4>)
                      '00 00 00 00'
                      '00 00 00 00'
                      'FF FF 00 00'
                      '01 00 00 00')

# pcap packet header that must preface every packet
pcap_packet_header = ('WW WW WW WW'  # Date
                      'ZZ ZZ ZZ ZZ'  # Microseconds
                      'XX XX XX XX'  # Frame Size (little endian)
                      'YY YY YY YY')  # Frame Size (little endian)

eth_header = ('00 00 00 00 00 00'  # Source Mac
              '00 00 00 00 00 00'  # Dest Mac
              '08 00')  # Protocol (0x0800 = IP)

ip_header = ('45'  # IP version and header length (multiples of 4 bytes)
             '00'
             'XX XX'  # Length - will be calculated and replaced later
             '00 00'
             '40 00 40'
             '11'  # Protocol (0x11 = UDP) / TCP = 0x6 / ICMP = 1 , pay attention values are HEX on the left 
             'YY YY'  # Checksum - will be calculated and replaced later
             'SS SS SS SS'  # Source IP (Default: 127.0.0.1)
             'DD DD DD DD')  # Dest IP (Default: 127.0.0.1)

udp_header = ('80 01'
              'XX XX'  # Port - will be replaced later
              'YY YY'  # Length - will be calculated and replaced later
              '00 00')


# this function returns byte length of HEX representation without spaces
def get_byte_length(str1):
    """Returns length in bytes """
    return len(''.join(str1.split())) / 2  # Q - WHY ? Answered above


# This function creates binary file after ,pcap is created
def write_byte_string_to_file(bytestring, filename):
    bytelist = bytestring.split()  # HEX STR-> LIST

    bytes = binascii.a2b_hex(''.join(bytelist))  # LIST -> BINARY STR

    bitout = open(filename, 'a+b')  # a - append , b - binary

    bitout.write(bytes)  # writing into binary file
    # Q - why file is not closed ?


def generate_pcap(message, factor, asset_ip, port, pcapfile):
    message *= factor
    print("len message: ", len(message))
    # %04x limiting string to 4 characters
    # udp = udp_header.replace('XX XX', "%04x" % port)
    udp = udp_header.replace('XX XX', "{}04x".format(port))
    # -Q why udp_len is in bytes ? A - value is required for checksum
    udp_len = get_byte_length(message) + get_byte_length(udp_header)

    # udp = udp.replace('YY YY', "%04x" % udp_len)
    udp = udp.replace('YY YY', "{}04x".format(udp_len))

    ip_len = udp_len + get_byte_length(ip_header)
    # ip = ip_header.replace('XX XX', "%04x" % ip_len)
    ip = ip_header.replace('XX XX', "{}04x".format(ip_len))

    # line below perform ip conversion from string to HEX octet by octet removing 0x from
    # the beginning adding  0 at the end of HEX representation, this is required for .pcap
    # zfill (2) means add 0 before first digit if the representation result is shorter then 1 digits

    # B  "B"-"E" i should rewrite this to separate function
    # dest_asset = " ".join([hex(int(value))[2:].zfill(2) for value in asset_ip.split('.')])
    dest_asset = " ".join([hex(int(value))[2:].zfill(2) for value in asset_ip.split('.')])

    # same as above HEX representation of source ip
    modified_src_ip = " ".join([hex(int(value))[2:].zfill(2) for value in SOURCE_IP.split('.')])

    ip = ip.replace('DD DD DD DD', dest_asset)
    ip = ip.replace('SS SS SS SS', modified_src_ip)

    # E
    # ip_checksum is defined below (its argument is ip_header)
    # that is replaced to "00 00" on the fly
    #
    checksum = ip_checksum(ip.replace('YY YY', '00 00'))

    # after checksum is calculated it is placed in header
    ip = ip.replace('YY YY', "%04x" % checksum)

    pcap_len = ip_len + get_byte_length(eth_header)  # total packet length that is required for checksums

    hex_str = "%08x" % pcap_len

    reverse_hex_str = hex_str[6:] + hex_str[4:6] + hex_str[2:4] + hex_str[:2]
    # Q- Why reverse hex_str is required ? A - https://en.wikipedia.org/wiki/Endianness
    # Different processors read bytes in different order
    # .pcap is built in such way that binary file should be written with reverse hex
    # Q - Why same reverse hex value is entered instead of XX and YY both ?
    # A - because thats how how .pcap was fuckin built
    pcaph = pcap_packet_header.replace('XX XX XX XX', reverse_hex_str)

    pcaph = pcaph.replace('YY YY YY YY', reverse_hex_str)
    # 28/07/2015 - STOP point

    time_list = str(datetime.utcnow()).split('.')  # splits miliseconds from timestamp
    # will replace milliseconds and date in pcap file

    counter = 0
    # for loop fills  .pcap file with packets , 1000 packets and insterval of 1 millisecond in between
    for i in range(NUMBER_OF_PACKETS - 1):  # Q -why -1 ?  A - Look @line  above
        counter += RESOLUTION  # ??
        current_pcap = copy.copy(
            pcaph)  # copy variable to new one in order to keep existinbg template e.g "WW WW WW WW "
        t = hex(int(time.mktime(time.strptime(time_list[0], '%Y-%m-%d %H:%M:%S'))) - time.timezone)[
            2:]  # HEX conversion of Day/Time
        little = ' '.join(t[x: x + 2] for x in range(0, len(t), 2))  # little endian
        big = little[9:] + little[5:9] + little[3:6] + little[0:2]  # big endian

        current_pcap = current_pcap.replace('WW WW WW WW',
                                            big)  # Q - Why ? A - because it worked , need to understand this later....
        msec = hex(int(0) + counter)[2:].zfill(8)  # HEX conversion of millisec
        little_msec = ' '.join(msec[x: x + 2] for x in range(0, len(msec), 2))  # little endian
        big_msec = little_msec[9:] + little_msec[5:9] + little_msec[3:6] + little_msec[0:2]  # big endian
        current_pcap = current_pcap.replace('ZZ ZZ ZZ ZZ', big_msec)

        if not os.path.exists(pcapfile):  # condition to create and write pcap header into file
            bytestring = pcap_global_header + current_pcap + eth_header + ip + udp + message  # total bytes to write into binary file
            write_byte_string_to_file(bytestring, pcapfile)

        bytestring = current_pcap + eth_header + ip + udp + message  # condition to write other headers besides pcap into existing file
        write_byte_string_to_file(bytestring, pcapfile)


# functions below are required for checksum calculation

# Splits the string into a list of tokens every n characters
def splitN(str1, n):
    return [str1[start:start + n] for start in range(0, len(str1), n)]


# Calculates and returns the IP checksum based on the given IP Header
def ip_checksum(iph):
    # split into bytes
    words = splitN(''.join(iph.split()), 4)

    csum = 0;
    for word in words:
        csum += int(word, base=16)

    csum += (csum >> 16)
    csum = csum & 0xFFFF ^ 0xFFFF  # XOR

    return csum  # this is required in each ip packet anew


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("not enough arguments")
        print("arg1 = Rate(Mbps)")
        print("arg2 = Run Time in sec")
        print("arg3 = Target Asset")
        print("arg4 = Target SDCC ip")
        print("arg5 = Target port")
        sys.exit(1)  # terminate - read pydoc

    # script CLI arguments
    mbps = sys.argv[1]
    run_time = int(sys.argv[2])
    asset = sys.argv[3]
    sdcc = sys.argv[4]
    netflow_port = sys.argv[5]

    # Calibration

    factor = 1000  # starting factor as packet length ("01*1000")
    start = datetime.utcnow()  # tuple with current UTC timestamp
    total_packets = 0  # initial packet value

    while not datetime.utcnow().second % CALIB_TIME == 0:  # (2015, 8, 3, 12, 26, 43, 458058) time sync with host time for start time , waiting until milliseconds mod calib_time without remainder
        time.sleep(0.1)
        # print "Wait until start: ",datetime.utcnow().second

    time.sleep(1)  # We want to start execution at the X1th second  , Q - why ?
    # A Prevents race condition # https://en.wikipedia.org/wiki/Race_condition
    print("Start Simulation")
    while datetime.utcnow() < start + timedelta(seconds=run_time):  # main loop

        if os.path.exists(PCAP_NAME):
            os.remove(PCAP_NAME)

        generate_pcap(message, factor, asset, port, PCAP_NAME)

        p = sub.Popen(
            ['softflowd', '-v', '5', '-r', 'pcap_file.pcap', '-n', '%s:%s' % (sdcc, netflow_port), '-T', 'full'],
            stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        print(output, errors)
        total_packets += NUMBER_OF_PACKETS  #
        iter_current = (datetime.utcnow())
        if iter_current.second % CALIB_TIME == 0:
            print("Total Packets: ", total_packets)
            PACKETS_PER_SEC = (total_packets / CALIB_TIME)
            print("Packets per second : ", PACKETS_PER_SEC)
            factor = int(round(float(mbps) / (8.0 * float(PACKETS_PER_SEC)), 4) * 1000000)  # pps to mbps conversion
            print("factor :%s , mbps :%s " % (factor, mbps))  # debug
            total_packets = 0
            time.sleep(1)
            print(
                "-----------------------------------------------------------------------------------------------------------------------------")
