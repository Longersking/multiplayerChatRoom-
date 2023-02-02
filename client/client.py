from windowLogin import *
from clientRequestProtocol import ResponseProtocol
from clientSocket import ClientSocket
from threading import Thread
from clientConfig import *
from tkinter.messagebox import showinfo


class Client(object):

    def __init__(self):
        """初始化客户端资源"""
        #初始化登陆窗口
        self.window = WindowLogin()
        self.window.onResetButtonClick(self.clearInput)
        self.window.onLoginButtonClick(self.sendLoginData)

        #创建客户端套接字
        self.conn = ClientSocket()

    def startup(self):
        #开始窗口主循环
        self.conn.connect()

        Thread(target=self.responseHandle).start()
        self.window.mainloop()

    def clearInput(self):
        """清空窗口内容"""
        self.window.clearUsername()
        self.window.clearPassword()

    def sendLoginData(self):
        """发送登陆消息到服务器"""
        #获取到用户输入的账号密码
        username = self.window.getUsername()
        password = self.window.getPassword()

        #生成协议文本
        requestText = ResponseProtocol.responseLoginResult(username,password)

        #发送协议文本到服务器
        #print("发送给服务器的文本为:"+requestText)
        self.conn.sendData(requestText)
        # recvData = self.conn.recvData()
        # print(recvData)

    def responseHandle(self):
        """不断接受服务器的新消息"""
        while True:
            recvData = self.conn.recvData()
            print("收到服务器消息:" + recvData)

            #解析数据
            responseData = self.parseResponseData(recvData)

            #根据消息响应判断消息请求类型
            if responseData["responseId"] == REQUEST_LOGIN_RESULT:
                #处理登录请求
                self.responseLoginHandle(responseData)
            elif responseData["responseId"] == REQUEST_CHAT_RESULT:
                #处理聊天请求
                self.responseChatHandle(responseData)

    @staticmethod
    def parseResponseData(recvData):
        """登录消息1001|登录状态|nickname|账号
           聊天消息1002|发送者昵称|消息内容
        """
        #使用协议约定的符号切割消息
        responseDataList = recvData.split(DELTMITER)

        #解析消息的各部分组成
        responseData = dict()
        responseData["responseId"] = responseDataList[0]

        if responseData["responseId"] == REQUEST_LOGIN_RESULT:
            #登录结果响应
            responseData["result"] = responseDataList[1]
            responseData["nickname"] = responseDataList[2]
            responseData["username"] = responseDataList[3]

        elif responseData["responseId"] == REQUEST_CHAT_RESULT:
            #聊天消息响应
            responseData["nickname"] = responseDataList[1]
            responseData["message"] = responseDataList[2]

        return responseData

    def responseLoginHandle(self,responseData):
        """登录结果响应"""
        print("接收到登陆信息~~",responseData)
        result = responseData["result"]
        if result == '0':
            showinfo("提示","登陆失败!账号或密码错误!")#标题,内容
            return

        showinfo("提示","登陆成功!")
        #登陆成功获取用户信息
        nickname = responseData["nickname"]
        username = responseData["username"]

        print("%s 的昵称为：%s,已经成功登陆"%(username,nickname))


    def responseChatHandle(self,responseData):
        """聊天结果响应"""
        print("接收到聊天消息~~",responseData)

if __name__ == '__main__':
    client = Client()
    client.startup()
