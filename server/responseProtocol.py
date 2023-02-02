from server.config import *

class ResponseProtocol(object):
    """服务器响应协议的格式字符串处理"""

    @staticmethod
    def responseLoginResult(result,nickname,username):
         """
         生成用户登录结果字符串
         :param result: 失败：0，成功：1
         :param nickname:用户登录的昵称，失败，则为空
         :param username:用户登录的账号，如果失败则为空
         :return:返回给用户的登录结果协议字符串
         """
         return DELTMITER.join([REQUEST_LOGIN_RESULT,result,nickname,username])

    @staticmethod
    def responseChat(nickname,messages):
        """
        生成给用户发的消息字符串
        :param nickname:发送消息的用户昵称
        :param message:消息正文
        :return:返回给用户的消息字符串
        """


        return DELTMITER.join([REQUEST_CHAT,nickname,messages])