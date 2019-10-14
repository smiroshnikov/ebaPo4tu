import _thread


def do_stuff(thread_id):
    while True:
        print("doing stuff.....", thread_id)


def start_program():
    i = 0
    while True:
        i += 1
        print(i)
        _thread.start_new_thread(do_stuff, (i,))

        if input() == 'q':
            break


start_program()


