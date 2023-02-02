from clientConfig import *

class ResponseProtocol(object):
    """服务器响应协议的格式字符串处理"""

    @staticmethod
    def responseLoginResult(username,password):
         """
        0001|user1|222
         """
         return DELTMITER.join([REQUEST_LOGIN,username,password])

    @staticmethod
    def responseChat(username,messages):
        """
        0002|user1|msg 类型|账号|消息内容
        """


        return DELTMITER.join([REQUEST_CHAT,username,messages])

