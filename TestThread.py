#!/usr/bin/env python3

import _thread
import time

def printMessage(message, id):
	print("Hello %s %d" % (message, id))
	time.sleep(2)

try:
	for i in range (1,5):
		message = ("Thread %i" % i) 
		print(message)
		_thread.start_new_thread(printMessage, ("Thread", i,))
except:
	print("Unable to start thread")

while 1:
	pass

