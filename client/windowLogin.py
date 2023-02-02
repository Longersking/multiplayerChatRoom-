from tkinter import Tk

class WindowLogin(Tk):
    """登录窗口"""

    def __init__(self):
        """初始化登录窗口"""
        super(WindowLogin, self).__init__()

        #设置窗口属性
        self.windowInit()

        #填充控件
        self.addWidgets()

    def windowInit(self):
        """初始化窗口的属性"""
        pass

    def addWidgets(self):
        """添加控件到窗口里"""
        pass