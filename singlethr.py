from time import sleep,ctime,time

def func1():
    i=0
    while i<=3:
        print “func1 at”, ctime(time())
        sleep(2)
        i=i+1

def func2():
    j=0
    while j<=3:
        print “func2 at”, ctime(time())
        sleep(1)
        j=j+1

print (‘*’*40)
print (“started at”, ctime(time()))
print (‘*’*40)

func1()
print (‘*’*40)

func2()
print (‘*’*40)
print (end at”, ctime(time()))
print (‘*’*40)
