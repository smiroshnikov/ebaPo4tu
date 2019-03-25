import threading
import time
from random import randint
from datetime import timedelta


def megafun(i):
    start = time.time()
    print(f"function called by thread {i}")
    result = i ** i ** i
    print(f"meaningless result is {result} time is {time.time()}")
    print(f"{threading.current_thread()}")
    end = time.time()
    elapsed = end - start
    print(f"{str(timedelta(seconds=elapsed))}")

    return


def yubaniy_nasos(i):
    start = time.time()
    # print(f"function called by thread {i}")
    # print(f"{threading.current_thread()}")
    time.sleep(randint(1, 20))
    end = time.time()
    elapsed = end - start
    print(f"{str(timedelta(seconds=elapsed))} : elapsed time for {threading.current_thread()}" )



threads = []
for i in range(5):
    # t = threading.Thread(target=megafun,
    #                      args=(i,)
    #                      )
    t = threading.Thread(target=yubaniy_nasos,
                         args=(i,)
                         )

    threads.append(t)
    t.start()
    # t.join()

