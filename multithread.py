from time import sleep,ctime,time
import thread

def func1():
    i=0
    while i<=3:
        print (“func1 at”, ctime(time()))
        sleep(2)
        i=i+1

def func2():
    j=0
    while j<=3:
        print (“func2 at”, ctime(time()))
        sleep(1)
        j=j+1

print (‘*’*40)
print (“started at”, ctime(time()))
print (‘*’*40)

thread.start_new_thread(func1,())
print (‘*’*40)

thread.start_new_thread(func2,())
sleep(9)

print (‘*’*40)
print (end at”, ctime(time()))
print (‘*’*40)
