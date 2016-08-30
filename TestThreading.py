#!/usr/bin/env python3

import threading
import time

class myThread (threading.Thread):
	def __init__(self, threadId, name, counter):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.counter = counter

	def run(self):
		print("Starting " + self.name)
		threadLock.acquire()
		print_time(self.name, 5, self.counter)
		threadLock.release()
		print("Exiting " + self.name)


def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		print("print_times: %s %s" % (threadName, time.ctime(time.time())))
		counter -= 1

threadLock = threading.Lock()

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("Exiting main thread")
