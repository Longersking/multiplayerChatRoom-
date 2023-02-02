from serverSocket import ServerSocket
from socketWrapper import  *
from responseProtocol import *
from server.dataBase import DataBase
import threading


class Server(object):
    """服务器核心类"""
    def __init__(self):
        #创建服务器套接字
        self.serverSocket = ServerSocket()

        #设置端口复用
        #self.serverSocket.setsockopt(self.serverSocket.SOL_SOCKET,self.serverSocket.SO_REUSEADDR,True)

        #创建保存当前用户登录信息的字典
        self.clientUserMessage = {}

        #创建数据库管理对象
        self.database = DataBase()

    def start(self):
        """获取客户端连接,并且提供服务"""
        while True:
            #获取客户端连接
            print("正在获取客户端连接...")
            soc,addr = self.serverSocket.accept()
            print("获取到客户端连接...")

            #使用套接字包装
            clientSocket = SocketWrapper(soc)

            #收发消息
            thread = threading.Thread(target=self.requestHandle,args=(clientSocket,))
            thread.start()

            #接收二进制数据
            #
            # recvData = soc.recv(512)
            # #将二进制数据转为字符串数据,并设置编码
            # recvContext = recvData.decode('utf-8')
            #
            # print(recvContext)
            #
            # soc.send("成功连接到服务器".encode('utf-8'))

            #关闭客户端套接字
            # soc.close()
    def requestHandle(self,clientSocket):
        while True:
            #接收客户端数据
            recvData = clientSocket.recvData()
            if not recvData:
                #客户端未发送消息
                self.removeOffClient(clientSocket)
                clientSocket.close()
                break
            #解析数据

            parseData = self.parseRequestData(recvData)

            #分析请求类型，并根据请求类型调用相关处理函数
            # print("获取到解析后内容：%s" % parseData)
            # # print(messages)
            # clientSocket.sendData("服务器收到的消息为：" + recvData)
            if parseData["requestId"] == REQUEST_LOGIN:
                #调用登录处理函数
                self.requestLoginHandle(clientSocket,parseData)
            elif parseData["requestId"] == REQUEST_CHAT:
                #调用聊天处理函数
                self.requestChatHandle(parseData)
            else:
                print("数据异常，无法解析")
                break


    def removeOffClient(self,clientSocket):
        """客户端下线后的处理"""
        print("客户端下线啦")
        #items()返回可遍历的（键，值）元组数组
        for username,info in self.clientUserMessage.items():
            if info["socket"] == clientSocket:
                print(self.clientUserMessage)
                del self.clientUserMessage[username]
                print(self.clientUserMessage)
                break


    def parseRequestData(self,recvData):
        """解析客户端发送来的数据

        登录信息：0001/username/password
        聊天信息:：0002/username/message
        """
        print("解析客户端数据:"+recvData)
        #创建请求列表，分割信息
        requestList = recvData.split(DELTMITER)

        #按类型解析数据
        requestData = {}

        requestData["requestId"] = requestList[0]

        if requestData["requestId"] == REQUEST_LOGIN:
            #用户请求登录
            requestData["username"] = requestList[1]
            requestData["password"] = requestList[2]

        elif requestData["requestId"] == REQUEST_CHAT:
            #用户请求聊天
            requestData["username"] = requestList[1]
            requestData["message"] = requestList[2]


        return requestData

    def requestLoginHandle(self,clientSocket,requestData):
        #处理登录功能的方法

        #获取对应的账号密码
        username = requestData["username"]
        password = requestData["password"]

        #检查是否可以登录
        ret,nickname,username = self.checkUserLogin(username,password)

        #登录成功，则需要保存当前用户
        if ret == '1':
            self.clientUserMessage[username] = {"socket":clientSocket,"nickname":nickname}

        #拼接返回给客户端的消息
        responseText = ResponseProtocol.responseLoginResult(ret,nickname,username)

        #把消息发送给客户端
        clientSocket.sendData(responseText)

    def requestChatHandle(self,requestData):
        #处理聊天功能的方法
        print("收到聊天消息~~~准备处理~~",requestData)

        #获取消息内容
        username = requestData["username"]
        message = requestData["message"]
        nickname = self.clientUserMessage[username]["nickname"]

        #拼接发送给客户端的消息文本
        sendMessage = ResponseProtocol.responseChat(nickname,message)

        #转发消息给在线用户
        for uName,info in self.clientUserMessage.items():
            #不需要向发送消息的账号转发消息
            if username == uName:
                continue
            info["socket"].sendData(sendMessage)


    def checkUserLogin(self,username,password):
        #检查登录是否成功的方法
        #从数据库查询用户信息
        sql = "select * from users where userName='%s'"%username
        result = self.database.getElement(sql)

        #没有查询结果则说明，用户不存在，登录失败
        if not result:
            return '0','',username

        #密码不匹配说明，密码错误，登录失败
        if password != result["userPassword"]:
            return '0', '', username


        #否则登录成功
        return '1',result["userNickname"],username


if __name__ == '__main__':
    server = Server()
    server.start()

