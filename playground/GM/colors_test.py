from time import sleep

from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
for t in range(0, 3):
    print(colored(f"FAKE DATA TESTS WILL START in {3-t}", 'yellow'))
    sleep(1)
