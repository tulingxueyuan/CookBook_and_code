import threading

sum = 0
loopSum = 1000000


lock = threading.Lock()


def myAdd():
    global  sum, loopSum

    for i in range(1, loopSum):
        # 上锁，申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()


def myMinu():
    global  sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))
