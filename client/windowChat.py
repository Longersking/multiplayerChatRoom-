from tkinter import Toplevel



class WindowChat(Toplevel):

    def __init__(self):
        super(WindowChat, self).__init__()
        #设置窗口大小，并且设置不可拉伸
        self.geometry("%dx%d"%(795,505))

        self.resizable(False,False)

        #添加组件
        self.addWidget()

    def addWidget(self):
        """添加组件方法"""
        pass

if __name__ == '__main__':
    WindowChat().mainloop()