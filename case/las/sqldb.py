import pymysql
import yaml

class sql_db():
      # def getConfig(self):
      #   with open('config.ymal',mode='r') as f:
      #       config = yaml.load(f,Loader=yaml.FullLoader)
      #       self.host = config['INNERSIT01']['host']
      #       #print(config['LASSIT01']['host'])
      #       self.port = config['INNERSIT01']['port']
      #       self.user = config['INNERSIT01']['user']
      #       self.pwd = config['INNERSIT01']['passwd']
      #       self.db = config['INNERSIT01']['db']

      def getDBConfig(self, environment, system):
          # 打开数据库配置文件
          print('getDBConfig ')
          with open('config.ymal', 'r') as file:
              # 获取数据库配置信息
              dbConfig = yaml.load(file, yaml.FullLoader)
              self.db = dbConfig[environment][system]
              self.host = dbConfig[environment]['host']
              self.port = dbConfig[environment]['port']
              self.user = dbConfig[environment]['user']
              self.passwd = dbConfig[environment]['passwd']
              return self.host, self.port, self.user, self.user, self.passwd, self.db

      def InnerModifyCredit(self,sql):
          print('InnerModifyCredit')
          try:
              #创建连接
              conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)

          except:
              raise  Exception('数据库连接失败！')
          # 创建游标并设置为字典类型
          curs = conn.cursor()
          curs.execute(sql)
          conn.commit()
          llll = curs.execute(sql)
          conn.commit()

          #查询结果集的第一行数据，返回一个元组
          # ret_one = curs.fetchone()
          #根据元组下标取出想要的值
          # cert_id = ret_one[0]
          # channel = ret_one[1]

          #读取结果集中的所有行，一行构成一个元组，然后再将这些元组返回 (('530624197906181945', 'Pbcc', '罗投拍'),) 里面括号是一个元组
          # resp_list = curs.fetchall()
          # #遍历元组，取出对应值
          # for row in resp_list:
          #     print('cert_id:%s\tchannel:%s\tname:%s' % row)

          conn.close()
          curs.close()




      def modifyDBdata(self,sql):
          # 创建链接
          conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)
          # 建立游标
          curs = conn.cursor()
          # 用游标执行SQL
          curs.execute(sql)

      def selectDBdata(self,sql):
          print('selectDBdata')
          # 创建链接
          conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)
          # 建立游标
          curs = conn.cursor()
          # 用游标执行SQL
          curs.execute(sql)
          result = curs.fetchone()
          return result
#
# db = sql_db()
# db.getDBConfig('SIT01','las')
#

