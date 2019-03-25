from time import sleep
from threading import Thread


class ThreadedHelloClass(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.message = f"Thread initialized ! {Thread.__str__(self)}"

    def print_message(self):
        print(self.message)

    def run(self):
        print(f"Thread Starting\n")
        x = 0
        while x < 20:
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended")


print("Process Started")
hello = ThreadedHelloClass()
hello.start()
print("Process Ended")
