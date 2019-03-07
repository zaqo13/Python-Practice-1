import time
import calendar

print('Number of ticks since 12.00 am, Jan 1970:',time.time())
localtime=time.localtime(time.time())
b=localtime[2]
print('edited time',b)
print('Detail Local current time:', localtime)
print('Local current time:',time.asctime())
print('calendar:\n',calendar.month(2008,1))
print('time.asctime():%s' % time.asctime(time.localtime()))

#by using this %time.mktime you can specify the time_struct that means full 9-digit ttime tuple
t=(1993,2,22,9,20,12,4,53,0)
secs=time.mktime(t)
print('\ntime.mktime(): %f'%secs)
print('asctime(localtime(secs)): %s'%time.asctime(time.localtime(secs)))
print('asctime(localtime(sec)):%s'%time.asctime(time.localtime(time.mktime(t))))

#this willgive you the delyed time in secs specify by the user
# print('Start: %s'% time.ctime())
# time.sleep(10)
# print('End: %s'%time.asctime()) #%time.ctime() OR %time.asctime()

#?????
# t=time.ctime(8)
# print('orignal time:%s'%time.asctime())
# print('time.ctime:%s'%t,type(t))

