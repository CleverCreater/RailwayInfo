import sqlite3


connect = sqlite3.connect('../data.sqlite')


class Exec:
    def __init__(self, sql):
        cursor = connect.cursor()
        try:
            cursor.execute(sql)
        except sqlite3.OperationalError as error:
            problem = error.__str__().split(':')
            if problem[0] == 'no such table':
                print('Please create table first')
            elif problem[0] == 'table User already exists':
                print('Already created')
            else:
                print(problem)
        cursor.close()
        connect.commit()
