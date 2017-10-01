# import time
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(3)
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
import time,datetime
TIME=datetime.datetime.now()
print(TIME)
time.sleep(2)
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))
time.sleep(2)
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))