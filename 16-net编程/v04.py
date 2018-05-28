import socket


def  tcp_srv():
    # 1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
    # 需要用到两个参数
    # AF_INET: 含义同udp一致
    # SOCK_STREAM: 表明是使用的tcp进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定端口和地址
    # 此地址信息是一个元祖类型内容，元祖分两部分，第一部分为字符串，代表ip，第二部分为端口，是一个整数，推荐大于10000
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)
    # 3. 监听接入的访问socket
    sock.listen()

    while True:
        # 4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
        # accept返回的元祖第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()
        # 5. 接受对方的发送内容，利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        #msg = skt.receive(500)
        msg = skt.recv(500)
        # 接受到的是bytes格式内容
        # 想得到str格式的，需要进行解码
        msg = msg.decode()

        rst = "Received msg: {0} from {1}".format(msg, addr)
        print(rst)
        # 6. 如果有必要，给对方发送反馈信息
        skt.send(rst.encode())

        # 7. 关闭链接通路
        skt.close()


if __name__ == "__main__":
    print("Starting tcp server.......")
    tcp_srv()
    print("Ending tcp server.......")
