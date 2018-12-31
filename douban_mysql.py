# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:17:55 2018

@author: 39660
"""

import MySQLdb as mysql

def mysql_open():
    # 快速建立数据库连接，返回连接对象
    connect = mysql.Connect(host="localhost",user="root",passwd="mysql",db="douban",charset='utf8')
    # 通过连接创建游标
    cursor = connect.cursor()
    return connect,cursor

def mysql_close(connect, cursor):
    if cursor:
        cursor.close()
    if connect:
        connect.close()
    
def insert_mysql(sql, params):
    print(sql)
    con,cur = None,None
    try:
        con,cur = mysql_open()
        cur.execute(sql, params)
        
        if cur.rowcount > 0:
            con.commit()
    except (Exception) as e:
        print('数据库访问出错:' + str(e))
    finally:
        mysql_close(con,cur)
        
def search_mysql(sql,params):
    con,cur = None,None
    try:
        con,cur = mysql_open()
        cur.execute(sql, params)
        
        return cur.fetchone()
    except (Exception) as e:
        print('数据库访问出错:' + str(e))
    finally:
        mysql_close(con,cur)
    
if __name__=="__main__":    
    sql = "insert into movies(name,type,url) values(%s,%s,%s)"
    insert_mysql(sql, ('test','剧情','HTTP'))

		
      