import socket
from clientConfig import *


class ClientSocket(socket.socket):
    """创建客户端套接字"""

    def __init__(self):
        #设置为tcp,ip4
        super(ClientSocket,self).__init__(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self):
        """自动连接服务器"""
        super(ClientSocket,self).connect((SERVER_IP,SERVER_PORT))

    def recvData(self):
        """接收数据，并自动转化为字符串"""
        return self.recv(512).decode("utf-8")

    def sendData(self,message):
        """发送数据"""
        return self.send(message.encode("utf-8"))