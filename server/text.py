import socket
from server.config import *

def test():
    #测试基本的服务器连接，数据发送，数据接收
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    client_socket.connect(('192.168.2.94',SERVER_PORT))
    while True:

        message = input("请输入你想输入的内容:")

        client_socket.send(message.encode('utf-8'))

        recv_data = client_socket.recv(512)

        print(recv_data.decode('utf-8'))

    client_socket.close()

if __name__ == '__main__':
    test()