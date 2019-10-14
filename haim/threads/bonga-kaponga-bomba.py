import threading
import time


def bonga(n):
    for i in range(0, n):
        print("bonga")
        time.sleep(1)



def kaponga(n):
    for i in range(0, n):
        print("kaponga")
        time.sleep(1)


def bomba(n):
    for i in range(0, n):
        print("bomba")
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=bonga, args=(10,))
    t2 = threading.Thread(target=kaponga, args=(10,))
    t3 = threading.Thread(target=bomba, args=(10,))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Done!")
