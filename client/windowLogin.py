from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import Button
from tkinter import LEFT

class WindowLogin(Tk):
    """登录窗口"""

    def __init__(self):
        """初始化登录窗口"""
        super(WindowLogin, self).__init__()

        #设置窗口属性
        self.windowInit()

        #填充控件
        self.addWidgets()

        self.onResetButtonClick(lambda : self.clearUsername())

        self.onLoginButtonClick(lambda : print(self.getUsername()))
    def windowInit(self):
        """初始化窗口的属性"""
        #设置窗口标题
        self.title("登陆窗口")

        #设置窗口不能被拉伸
        self.resizable(False,False)

        #获取窗口位置的变量
        windowWidth = 255
        windowHeight = 95

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        posX = (screenWidth - windowWidth)/2
        posY = (screenHeight - windowHeight)/2

        #设置窗体大小不能改变
        self.geometry("%dx%d+%d+%d"%(windowWidth,windowHeight,posX,posY))

        #窗口宽高

        #屏幕宽高

        #屏幕中心坐标位置


        #设置窗口大小和位置


    def addWidgets(self):
        """添加控件到窗口里"""
        #用户名
        #文本标签
        usernameLabel = Label(self)
        usernameLabel["text"] = "用户名:"
        #设置显示位置,pad表示边距，前俩个参数表示第几行第几列
        usernameLabel.grid(row=0,column=0,padx=10,pady=5)
        #设置文本框
        usernameEntry = Entry(self,name="usernameEntry")
        usernameEntry.grid(row=0,column=1)

        #设置文本框显示长度
        usernameEntry["width"] = 25

        #密码
        passwordLabel = Label(self)
        passwordLabel["text"] = "密   码:"
        passwordLabel.grid(row=1,column=0)
        passwordEntry = Entry(self,name="passwordEntry")
        passwordEntry.grid(row=1,column=1)
        passwordEntry["width"] = 25
        #密码显示不为明文
        passwordEntry["show"] = '*'

        #按钮区
        buttonFrame = Frame(self,name="buttonFrame")

        #重置按钮
        resetButton = Button(buttonFrame,name="resetButton")
        resetButton["text"] = " 重置 "
        resetButton.pack(side=LEFT,padx=20)

        #登陆按钮
        loginButton = Button(buttonFrame,name="loginButton")
        loginButton["text"] = " 登陆 "
        loginButton.pack(side=LEFT)

        buttonFrame.grid(row=2,columnspan=2,pady=5)

    def onLoginButtonClick(self,command):
        #为登陆按钮添加事件响应
        loginButton = self.children["buttonFrame"].children["loginButton"]
        loginButton["command"] = command

    def onResetButtonClick(self,command):
        #为重置按钮添加事件响应
        resetButton = self.children["buttonFrame"].children["resetButton"]
        resetButton["command"] = command

    def getUsername(self):
        """获取用户名"""
        return self.children["usernameEntry"].get()

    def getPassword(self):
        """密码"""
        return self.children["passwordEntry"].get()

    def clearUsername(self):
        """清空用户名"""
        self.children["usernameEntry"].delete(0, "end")

    def clearPassword(self):
        """清空密码"""
        self.children["passwordEntry"].delete(0, "end")

    def onWindowClosed(self,command):
        """窗口关闭事件处理方法"""

        #设置窗口关闭事件
        self.protocol("WM_DELETE_WINDOW",command)

if __name__ == '__main__':
    window = WindowLogin()
    window.mainloop()