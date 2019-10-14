import threading
import time


class MyThread(threading.Thread):
    def __init__(self, str, number, daemon):
        threading.Thread.__init__(self)
        self.str = str
        self.number = number
        self.daemon = daemon
        if daemon:
            self.setDaemon(daemon)

    def run(self):
        i = 1
        while i < self.number:
            time.sleep(2)
            print(self.str)
            i = i + 1


a = MyThread("gaga not daemon", 10, False)
a.start()
b = MyThread("mama daemon ", 100, True)
b.start()

# process is a collection of threads
# background thread and foreground thread is more ?common? way of naming those


