#!/usr/bin/env python3
import time
import sqlite3

sql_create_table = '''CREATE TABLE IF NOT EXISTS `battery`(
       timestamp INT,
       remain INT,
       capacity INT,
       cycle_count INT,
       charging BOOL,
       type VARCHAR(10)
       );
'''


class Operator():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def init_table(self):
        self.c.execute(sql_create_table)
        self.conn.commit()

    def insert_record(self, t):
        sql = f'''INSERT INTO `battery` (timestamp, remain, capacity, cycle_count, charging, type)
                              VALUES ({int(time.time())}, ?, ?, ?, ?, ?)'''
        self.c.execute(sql, t)
        self.conn.commit()


db = Operator('battery.db')


if __name__ == '__main__':
    db.init_table()
    t = (3000, 3777, 200, True, "mock")
    db.insert_record(t)

