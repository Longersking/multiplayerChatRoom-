


class SocketWrapper(object):
    """套接字包装类"""
    def __init__(self,argSocket):
        self.socket = argSocket

    def recvData(self):
        """接收数据"""
        try:
            return self.socket.recv(512).decode('utf-8')
        except:
            return ""

    def sendData(self,message):
        return self.socket.send(message.encode('utf-8'))

    def close(self):
        #关闭套接字
        self.socket.close()