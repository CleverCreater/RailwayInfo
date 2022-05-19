import pymysql


connection = pymysql.connect(
    user='Andy',
    password='123456',
    host='192.108.101.29',
    database='RailwayInfo',
)


cursor = connection.cursor()


cursor.execute('''

''')
