import threading
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for x in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for x in range(5):
            print("Hi")
            sleep(1)
t1=Hello()
t2=Hi()

t1.start()
t2.start()
print("Total number of threads:" ,threading.active_count())
t1.join()
t2.join()
print("Total number of threads-2:" ,threading.active_count())

print("---DONE---")

#print(help(Thread))