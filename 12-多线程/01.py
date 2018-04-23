'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间

'''
import time

def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


def main():
    print("Starting at:", time.ctime())
    loop1()
    loop2()
    print("All done at:", time.ctime())


if __name__ == '__main__':
    main()

