import threading
import time
def T1_job():
    print ('T1 start')
    for i in range(10):
        time.sleep(0.2)
    print('T1 is done')

def T2_job():
    print ('T2 starts')
    print('T2 is done')
def main():
    added_thread=threading.Thread(target=T1_job,name='T1')
    added_thread.start()
    added_thread.join()  #join 可以选择线程进行顺序
    thread2=threading.Thread(target=T2_job,name='T2').start()


if __name__ == '__main__':
    main()