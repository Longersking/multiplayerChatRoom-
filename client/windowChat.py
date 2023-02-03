from tkinter import Toplevel
from tkinter.scrolledtext import ScrolledText
from tkinter import Text
from tkinter import Button
from tkinter import UNITS
from tkinter import END
from time import localtime,strftime,time



class WindowChat(Toplevel):

    def __init__(self):
        super(WindowChat, self).__init__()
        #设置窗口大小，并且设置不可拉伸
        self.geometry("%dx%d"%(795,505))

        self.resizable(False,False)

        self.setTitle("longersking")
        #添加组件
        self.addWidget()

        #self.onSendButtonClick(lambda :self.appendMessage("longersking","hello"))
    def addWidget(self):
        """添加组件方法"""
        #聊天区
        chatTextArea = ScrolledText(self)
        chatTextArea["width"] = 110
        chatTextArea["height"] = 30
        chatTextArea.grid(row=0,column=0,columnspan=2)

        #发送区
        chatInputArea = Text(self,name="chatInputArea")
        chatInputArea["width"] = 100
        chatInputArea["height"] = 7
        chatInputArea.grid(row=1,column=0,pady=10)

        #设置字体颜色
        chatTextArea.tag_config("green",foreground="#008B00")
        chatTextArea.tag_config("system",foreground="red")
        self.children["chatInputArea"] = chatInputArea
        self.children["chatTextArea"] = chatTextArea
        #发送按钮
        sendButton = Button(self,name="sendButton")
        sendButton["text"] = "发送"
        sendButton["width"] = 5
        sendButton["height"] = 2
        sendButton.grid(row=1,column=1)


    def setTitle(self,title):
        """设置文本框标题"""
        self.title("欢迎%s进入聊天室"%title)

    def onSendButtonClick(self,command):
        """注册事件，当按下发送按钮的时候执行command的方法"""
        self.children["sendButton"]["command"] = command

    def getInput(self):
        """获取输入框内容"""
        return self.children["chatInputArea"].get(0.0,END)

    def clearInput(self):
        """清空文本框"""
        self.children["chatInputArea"].delete(0.0,END)

    def appendMessage(self,sender,message):
        """添加一条消息到聊天区"""
        sendTime = strftime("%Y-%m-%d %H:%M:%S",localtime(time()))
        sendInfo = "%s: %s\n"%(sender,sendTime)

        self.children["chatTextArea"].insert(END,sendInfo,"green")
        self.children["chatTextArea"].insert(END," " + message + "\n")

        #向下滚动屏幕
        self.children["chatTextArea"].yview_scroll(3,UNITS)

    def onCloseWindowClient(self,command):
        """关闭窗口释放资源"""
        self.protocol("WM_DELETE_WINDOW",command)




if __name__ == '__main__':
    WindowChat().mainloop()