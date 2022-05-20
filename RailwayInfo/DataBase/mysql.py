import pymysql


class MysqlUtil:
    def __init__(self):
        self.db = pymysql.connect(
            user='boss',
            password='control',
            host='192.108.101.29',
            database='RailwayInfo',
        )
        self.cursor = self.db.cursor()

    def insert(self, sql):
        """
        插入数据库
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except pymysql.Error:
            self.db.rollback()
        finally:
            self.db.close()

    def fetchone(self, sql):
        """
        查询数据库(单)
        :param sql:
        :return:
        """
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except pymysql.Error:
            self.db.rollback()
        finally:
            self.db.close()
        return result

    def fetchall(self, sql):
        """
        查询数据库(多)
        :param sql:
        :return:
        """
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except pymysql.Error:
            self.db.rollback()
        finally:
            self.db.close()
        return result

    def delete(self, sql):
        """
        删除
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except pymysql.Error:
            self.db.rollback()
        finally:
            self.db.close()

    def update(self, sql):
        """
        更新
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except pymysql.Error:
            self.db.rollback()
        finally:
            self.db.close()
