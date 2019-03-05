from time import localtime, strftime, mktime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")
input("Press ENTER key to stop timer ")
stop_time = localtime()
diff = mktime(stop_time) - mktime(start_time)
print(f"Timer stopper at {strftime('%X', stop_time)}")
print(f"Total time {diff} seconds")
