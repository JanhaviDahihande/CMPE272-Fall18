#!/usr/bin/python3

import requests
import threading
import time

exitThread = 0

#Creating thread class
class thread(threading.Thread):
    def __init__(self, threadName):
      threading.Thread.__init__(self)
      self.threadName = threadName

    def run(self):
        print_date(self.threadName)

#Function to start threads
def startThreads():
    firstThread.start()
    secondThread.start()
    thirdThread.start()

#Function to join threads
def joinThreads():
    firstThread.join()
    secondThread.join()
    thirdThread.join()

#Printing request Date
def print_date(threadName):
        if exitThread:
            threadName.exit()
        request = requests.get("https://webhook.site/c49f0bdc-3c0b-4718-81fa-053b5fddc5aa")
        print('Thread: %s : %s' % (threadName,request.headers['Date']))

#Creating threads
firstThread = thread("First Thread")
secondThread = thread("Second Thread")
thirdThread = thread("Third Thread")

#Starting and Joining
startThreads()
joinThreads()



