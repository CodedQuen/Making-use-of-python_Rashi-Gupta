from time import sleep, ctime, time
import threading

class MyThread(threading.Thread):
    def run(self):
        number =1
        while(number <= 5):
            print”Thread executing”,ctime(time())
            sleep(1)
            number=number+1
threadarray = []
threadnumber = 1
while threadnumber <= 2:
    NewThreadObject = MyThread()
    NewThreadObject.start()
    threadarray.append(NewThreadObject)
    threadnumber=threadnumber+1
for mythread in threadarray:
    mythread.join()
print (“End of My Code”)
