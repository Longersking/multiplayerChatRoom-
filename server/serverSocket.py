#创建服务端套接字，传递消息！
import socket
from serverConfig import *

class ServerSocket(socket.socket):
    """初始化服务器需要的套件字,负责套接字所需要的相关参数"""
    def __init__(self):
        # #ip4,tcp的方式创建套接字
        # self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # #绑定ip地址和设置端口号
        # self.socket.bind(ip,port)
        # #设置监听客户端连接数量
        # self.socket.listen(128)
        #这里可以直接调用父类方法
        #设置TCP协议套接字
        super(ServerSocket,self).__init__(socket.AF_INET,socket.SOCK_STREAM,)
        #设置端口号，和ip地址
        self.bind((SERVER_IP,SERVER_PORT))
        #设置监听模式
        self.listen(128)


