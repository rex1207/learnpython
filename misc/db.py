import mysql.connector
#连接数据库
config = {
    'user' : 'root',       #用户名
    'password' : 'lazio2000', #自己设定的密码
    'host' : '127.0.0.1',    #ip地址，本地填127.0.0.1，也可以填localhost
    'port' : '3306',        #端口,mysql默认3306
    'database' : 'stock'   #数据库名字
}
con = mysql.connector.connect(**config)
print(con)
cursor = con.cursor()
query = 'select * from price'
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
import datetime
# now = datetime.datetime.now()
# print(now)
insert = '''insert into price values('2022-02-26 20:44:21', 10.11,10.22,'600030')'''
cursor.execute(insert)
con.commit()
