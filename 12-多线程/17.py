import threading
import time

def func():
    print("I am running.........")
    time.sleep(4)
    print("I am done......")



if __name__ == "__main__":
    t = threading.Timer(6, func)
    t.start()

    i = 0
    while True:
        print("{0}***************".format(i))
        time.sleep(3)
        i += 1
