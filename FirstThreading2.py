import time
import threading


start = time.perf_counter()

def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done Sleeping')

#1 part
do_something()
do_something()
do_something()

#2 part
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# #t3 = threading.Thread(target=do_something)

# t1.start()
# t2.start()
# #t3.start()
# t1.join()
# t2.join()

#3 Part
# threads = []
# for _ in range(10):
# 	t = threading.Thread(target=do_something)
# 	t.start()
# 	threads.append(t)
# for thread in threads:
# 	thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


#io bound and - utilizing input and output process.
#process bound - utilize more cpu process

