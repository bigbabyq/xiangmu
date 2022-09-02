import cursor as cursor
import flask
from flask import Flask, render_template, request, redirect, url_for, session, g
from flask import Flask
import pymysql
from dataclasses import dataclass

app = Flask(__name__)


db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='hq261328', database='超市仓储管理信息系统', charset='utf8')
# 操作数据库，获取db下的cursor对象
cursor = db.cursor()
def conn():
    conn = pymysql.connect(
        host="127.0.0.1",
        user='root',
        password='hq261328',
        port=3306,
        db='超市仓储管理信息系统',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8'
    )
    return conn

@app.route('/chukuchaxun', methods=['GET', 'POST'])
def chukuchaxun():
    query_result = ''
    results = ''
# 获取下拉框的数据
    if flask.request.method == 'POST':
        select = flask.request.form.get('selected_one')
        query = flask.request.values.get('query')
        print(select, query)
        # 判断不同输入对数据表进行不同的处理
        if select == '货物编号':
            try:
                sql = "select * from chukudan where xuhao = %s; "
                cursor.execute(sql, query)
                results = cursor.fetchall()
                if results:
                    query_result = '查询成功!'
                else:
                    query_result = '查询失败!'
            except Exception as err:
                print(err)
                pass
        if select == '货物名称':
            try:
                sql = "select * from chukudan where mingcheng = %s; "
                cursor.execute(sql, query)
                results = cursor.fetchall()
                if results:
                    query_result = '查询成功!'
                else:
                    query_result = '查询失败!'
            except Exception as err:
                print(err)
                pass
        if select == '入库签收员':
            try:
                sql = "select * from chukudan where beizhu = %s; "
                cursor.execute(sql, query)
                results = cursor.fetchall()
                if results:
                    query_result = '查询成功!'
                else:
                    query_result = '查询失败!'
            except Exception as err:
                print(err)
                pass

    return flask.render_template('数据管理---出库单查询.html', query_result=query_result, results=results)

try:
    app.run()
except Exception as err:
    print(err)
    db.close()  # 关闭数据库连接

if __name__ == '__main__':
    app.run()
