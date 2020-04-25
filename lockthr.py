import thread
from time import ctime,time,sleep

class Bank:
    def __init__(self):
        self._account={}
        self._account[‘1’]=self.account_savings
        self._account[‘2’]=self.account_current
        self._account[‘3’]=self.account_fixed
        self._account[‘4’]=self.account_recrg
    def account(self,selection,seconds):
        self._account[selection](seconds)
    def account_savings(self,seconds_arg):
        thread.start_new_thread(self.openac,(seconds_arg,\
                                    ‘1. Savings’,locks[0]))
    def account_current(self,seconds_arg):
        thread.start_new_thread(self.openac,(seconds_arg,\
                                    ‘2. Current’,locks[1]))
    def account_fixed(self,seconds_arg):
        thread.start_new_thread(self.openac,(seconds_arg,\
                                    ‘3. Fixed’,locks[2]))
    def account_recrg(self,seconds_arg):
        thread.start_new_thread(self.openac,(seconds_arg,\
                                    ‘4. Recurring’,locks[3]))
    def openac(self,seconds,account,lock):
        for i in range(seconds):
            sleep(0.01)
            print (“%s is opened at %s” % (account,ctime(time())))
myBank=Bank()
locks=[]
for i in range(4):
    lock=thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
print (“start at”,ctime(time()))
myBank.account(‘1’,700)
myBank.account(‘2’,500)
myBank.account(‘3’,500)
myBank.account(‘4’,300)
