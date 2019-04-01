# need install snmpsimd from sourceforge
# no further requirements

import sys
import argparse
import subprocess
import os
from my_mib_tree import my_mib # still not what I wanted , however this will work as traffic simulator on any machine

def mib_create(bw,community="public"):
    """
    packets = this variable represents Gigabit1 interface packets
    bw =  this variable represents Gigabit1 interface bandwidth
    """
    packets = (bw*131072/512)
    packets2 = str(packets/2) # Q -why converting to string? A - all inputs are converted to str (YairG)
    bw2 = str(bw*131072/2) # Q -why converting to string? A - answered above !
    bw=str(bw*131072)
    packets=str(packets) # Q- is this even fucking possible ? A- yes ! common ground


    with open('public.snmprec','w') as mib_file: # needs to be redone , I wont to work with file and not string object
        mib_file.write(my_mib%(bw,bw2,packets,packets2,bw,bw2,packets,packets2,bw,bw2,packets,packets2,bw,bw2,packets,packets2))


def start_simulation(timeout,ip): # Read documentation on os.system
    """
    CLI processing
    """
    os.system('\cp /home/public.snmprec /usr/snmpsim/data/public.snmprec')
    os.system('killall snmpsimd.py')
    # please explain line below
    # subprocess arguments are lists , subprocess.Popen works best with list
    #
    # $> will translate to "timeout 300 " , snmpsimd location , execution permissions , port and ip , output is piped to stdout
    p = subprocess.Popen(['timeout','%s'%timeout,'/usr/bin/snmpsimd.py','--agent-udpv4-endpoint=%s:161'%ip,'--process-user=root','--process-group=root'],stdout=subprocess.PIPE)

    # this is parsing of output
    while True:
        output = p.stdout.readline()
        if output == '' and p.poll() is not None:
            break
        if output:
            print output
    rc = p.poll()
    return rc # what rc represents ? rc = return call (read linux documentation on return calls)



if __name__== "__main__": # run following code only from traffic_simulator.py
    #    ip = '127.0.0.1'
    ip = '10.20.5.222' # IP needs to be chaged to machine ip that simulator run on
    parser = argparse.ArgumentParser()
    # required might overwrite default , should check python docs...
    parser.add_argument('-b',help="Desired Traffic Bandwidth",type=int,required=True,default=500)
    # time in seconds
    parser.add_argument('-t',help="simulation runtime",required=True)
    parser.add_argument('-c',help="Community name. (default is 'public')",default="public")
    # args input
    args = parser.parse_args()

    print "BW: ",args.b
    print "community: ",args.c
    print "timeout: ",args.t
    mib_create(args.b,args.c)

    # ip = os.system("ip route get 8.8.8.8 | head -1 | cut -d' ' -f8")
    start_simulation(args.t,ip)