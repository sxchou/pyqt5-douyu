import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='zsxmysql262728',
                       database='users',
                       charset='utf8')

cursor = conn.cursor()
username = 'admin'
password = 284611
sql = f'select * from users where username="{username}" and password="{password}"'
result = cursor.execute(sql)
print(result)
