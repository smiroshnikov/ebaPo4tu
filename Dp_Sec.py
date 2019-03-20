import datetime
import time
import argparse
import random
import string

MY_SQL = 'mysql'
ELASTIC_SEARCH = 'elastic'

ELASTIC_DOC_TYPE = 'traffic-raw'

PACKETS_PER_SECOND = 'pps'
BITS_PER_SECOND = 'bps'

MONITORING_PROTOCOL = 'all'  # [tcp, udp, icmp, sctp, other, all]
DIRECTION = 'Inbound'

TRAFFIC_MONITORING_PROTOCOL = 5  # all protocols
POLICY_DIRECTION = 1
NULL = 'NULL'
DTYPE = NULL


def GetElasticSearchIndexName():
    return 'dp-' + ELASTIC_DOC_TYPE + '-' + str(int(time.time() / 3600))


def GetElasticSearchIndexID():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))


def SimulateDPTrafficUtilization(policy, port, deviceIP, rate, duration, unit, elasticsearch=None):
    if elasticsearch:
        from elasticsearch import Elasticsearch
        es = Elasticsearch(elasticsearch)
        index = GetElasticSearchIndexName()
        if not es.indices.exists(index):
            print('Index: [' + index + '] is not found in elasticsearch.')
            return 1

        if policy:
            port = '-1'
        else:
            policy = 'NO_POLICY'

        if unit == PACKETS_PER_SECOND:
            traffic_value = rate
        else:
            traffic_value = rate * 1000

        discards = traffic_value / 2
        excluded = traffic_value / 2

        for x in range(duration * 60):
            doc = {
                'id': None,
                'deviceIp': deviceIP,
                'physicalPort': port,
                'policyName': policy,
                'direction': DIRECTION,
                'trafficValue': traffic_value,
                'discards': discards,
                'excluded': excluded,
                'unit': unit,
                'monitoringProtocol': MONITORING_PROTOCOL,
                'timeStamp': int(
                    round((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)),
                'minuteOfDay': datetime.datetime.utcnow().hour * 60 + datetime.datetime.utcnow().minute
            }

            res = es.index(index=index, doc_type=ELASTIC_DOC_TYPE, id=GetElasticSearchIndexID(), body=doc)
            time.sleep(1)

            if unit == PACKETS_PER_SECOND:
                print('[DP traffic utilization %02d:%02d] - device: %s, rate: %d pps, policy: %s' % (
                    (x + 1) / 60, (x + 1) % 60, deviceIP, rate, policy))
            else:
                print('[DP traffic utilization %02d:%02d] - device: %s, rate: %0.3f Mbps, policy: %s' % (
                    (x + 1) / 60, (x + 1) % 60, deviceIP, rate, policy))
    else:
        import pymysql
        pymysql.install_as_MySQLdb()
        import MySQLdb

        db = MySQLdb.connect('127.0.0.1', "securitydam", "securitydam", "vision")
        cursor = db.cursor()

        if unit == PACKETS_PER_SECOND:
            unit_id = 2  # rate in pps (packets per second)
            traffic_value = rate
        else:
            unit_id = 1  # rate in bps (Mb per second)
            traffic_value = rate * 1000

        num_discards = traffic_value / 2
        num_excluded = traffic_value / 2

        for x in range(duration * 60):
            time_stamp = datetime.datetime.utcnow()
            orm_id = str(random.randint(1, 9)) + str(int(round(time.time() * 1000)))

            if policy:
                query = """ INSERT INTO vision.traffic_utilizations_per_policy
                                (orm_id,
                                 physical_port,
                                 policy_name,
                                 policy_direction,
                                 traffic_value,
                                 num_discards,
                                 num_excluded,
                                 unit_id,
                                 traf_mon_protocols,
                                 time_stamp,
                                 device_ip,
                                 DTYPE)
                                VALUES (\'%s\', %s, \'%s\', %d, %d, %d, %d, %d, %d, \'%s\', \'%s\', %s); """ % \
                        (orm_id,
                         NULL,
                         policy,
                         POLICY_DIRECTION,
                         traffic_value,
                         num_discards,
                         num_excluded,
                         unit_id,
                         TRAFFIC_MONITORING_PROTOCOL,
                         time_stamp,
                         deviceIP,
                         DTYPE)

                lock_query = 'LOCK TABLES traffic_utilizations_per_policy write;'
            else:
                query = """ INSERT INTO vision.traffic_utilizations
                            (orm_id,
                             physical_port,
                             policy_name,
                             policy_direction,
                             traffic_value,
                             num_discards,
                             num_excluded,
                             unit_id,
                             traf_mon_protocols,
                             time_stamp,
                             device_ip,
                             DTYPE)
                            VALUES (\'%s\', %d, %s, %d, %d, %d, %d, %d, %d, \'%s\', \'%s\', %s); """ % \
                        (orm_id,
                         1,
                         NULL,
                         POLICY_DIRECTION,
                         traffic_value,
                         num_discards,
                         num_excluded,
                         unit_id,
                         TRAFFIC_MONITORING_PROTOCOL,
                         time_stamp,
                         deviceIP,
                         DTYPE)

                lock_query = 'LOCK TABLES traffic_utilizations write;'
            try:
                cursor.execute(lock_query)
                db.commit()

                cursor.execute(query)
                db.commit()

                cursor.execute('UNLOCK TABLES;')
                db.commit()
            except Exception as e:
                print(e)

            time.sleep(1)

            if unit == PACKETS_PER_SECOND:
                print('[DP traffic utilization %02d:%02d] - device: %s, rate: %d pps, policy: %s' % (
                    (x + 1) / 60, (x + 1) % 60, deviceIP, rate, policy))
            else:
                print('[DP traffic utilization %02d:%02d] - device: %s, rate: %0.3f Mbps, policy: %s' % (
                    (x + 1) / 60, (x + 1) % 60, deviceIP, rate, policy))

        db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--rate', metavar='\b', help="Rate (in Mbps/pps).", type=float, required=True)
    parser.add_argument('--duration', metavar='\b', help="Simulation duration (in minutes) Default: 5 min.", type=int,
                        default=5, required=False)
    parser.add_argument('--policy', metavar='\b', help="Policy name.", required=False, default=None)
    parser.add_argument('--port', metavar='\b', help="Physical port name.", required=False, default=None)
    parser.add_argument('--device', metavar='\b', help="IP address of CPE/device.", required=True)
    parser.add_argument('--unit', metavar='\b',
                        help=BITS_PER_SECOND + ' | ' + PACKETS_PER_SECOND + '. Default: ' + BITS_PER_SECOND + '.',
                        default=BITS_PER_SECOND, required=False)
    parser.add_argument('--elastic', metavar='\b', help='Elasticsearch IP address.', default=None, required=False)
    args = parser.parse_args()

    if args.unit == 'pps':
        print('\nSimulating DP traffic utilization for %d minutes (rate~%d pps) ...\n' % (args.duration, args.rate))
    else:
        print('\nSimulating DP traffic utilization for %d minutes (rate~%0.3f Mbps) ...\n' % (args.duration, args.rate))

    SimulateDPTrafficUtilization(args.policy, args.port, args.device, args.rate, args.duration, args.unit, args.elastic)
