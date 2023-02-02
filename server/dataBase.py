from pymysql import connect
from server.config import *

#操作数据库的类
class DataBase(object):

    def __init__(self):
        #连接到数据库
        self.conn = connect(
                host=DATABASE_HOST,
                port=DATABASE_PORT,
                database=DATABASE_NAME,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                )

        #获取游标
        self.cursor = self.conn.cursor()

    def getElement(self,sql):
        #获取用户信息
        #执行sql语句
        self.cursor.execute(sql)

        #获取查询结果
        queryResult = self.cursor.fetchone()

        #判断是否有结果
        if not queryResult:
            return None

        #获取字段
        fileds = [filed[0] for filed in self.cursor.description]

        #使用字段和数据合成字典
        returnData = {}
        for filed,value in zip(fileds,queryResult):
            returnData[filed] = value

        return returnData


    def close(self):
        #关闭数据库
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':
    database = DataBase()
    data = database.getElement("select * from users WHERE userName='longersking'")
    print(data)
    database.close()
