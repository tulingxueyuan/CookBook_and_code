import time,re,fcntl
import os,datetime
from concurrent import futures

count_list = list()
MinuteNum = 1
StartTime = datetime.datetime(2018, 5, 1, 19, 31, 0, 484870)
NowTime = datetime.datetime.now()
os.system(':>new.txt')

f_new = open('new.txt','a')

def conc(CountTimeFormat):
   f = open('push_slave.stdout', 'r')
   for line in f.readlines():
       if re.search(CountTimeFormat,line):
           #获得文件专用锁
           fcntl.flock(f_new, fcntl.LOCK_EX)
           f_new.writelines(line)
           f_new.flush()
           #释放文件锁
           fcntl.flock(f_new, fcntl.LOCK_UN)
           break

while 1:
   AfterOneMinute = datetime.timedelta(minutes=MinuteNum)
   CountTime = AfterOneMinute + StartTime
   CountTimeFormat = CountTime.strftime('%Y-%m-%d %H:%M')
   MinuteNum = MinuteNum+1
   count_list.append(CountTimeFormat)
   if CountTimeFormat == "2018-05-2 16:00":
       break

def exec_cmd():
   with futures.ProcessPoolExecutor(max_workers=24) as executor:
       dict(( executor.submit(conc, times), times) for times in count_list)

if __name__ == '__main__':
   exec_cmd()
   f_new.close()