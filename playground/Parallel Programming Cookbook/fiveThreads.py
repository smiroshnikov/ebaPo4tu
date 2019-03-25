import threading
import time


def megafun(i):
    print(f"function called by thread {i}")
    result = i ** i ** i
    print(f"meaningless result is {result} time is {time.time()}")
    return


threads = []
for i in range(5):
    t = threading.Thread(target=megafun,
                         args=(i,)
                         )
    threads.append(t)
    t.start()
    t.join()
