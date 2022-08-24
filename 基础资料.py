from flask import Flask, render_template, request, redirect, app
import pymysql

app = Flask("代办项网站")
def conn():
    conn = pymysql.connect(
        host="127.0.0.1",
        user='root',
        password='hq261328',
        port=3306,
        db='超市仓储管理信息系统',
        charset='utf8'
    )
    return conn

#基础资料
@app.route('/')
def ziliao():
    return render_template('基础资料.html')

#供应商资料
def paixu_gongyingshang():
    conn1 = conn()
    sql="""
    select * from gongyingshangziliao
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_gongyingshang(id):
    #从数据库查询单条数据
    conn1 = conn()
    sql = f"""
        select * from gongyingshangziliao
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

@app.route('/gongyingshang', methods = ["GET", "POST"])
def gongyingshangchaxun():
    datas = paixu_gongyingshang()
    return render_template("供应商资料.html", datas=datas)

#产品资料
def paixu_chanpin():
    conn1 = conn()
    sql="""
    select * from chanpinziliao
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_chanpin(id):
    conn1 = conn()
    #从数据库查询单条数据
    sql = f"""
        select * from chanpinziliao
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

@app.route('/chanpin', methods = ["GET", "POST"])
def chanpinchaxun():
    datas = paixu_chanpin()
    return render_template("产品资料.html", datas=datas)

#员工信息
def paixu_yuangong():
    conn1 = conn()
    sql="""
    select * from yuangongxinxi
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_yuangong(id):
    conn1 = conn()
    #从数据库查询单条数据
    sql = f"""
        select * from yuangongxinxi
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

@app.route('/yuangong', methods = ["GET", "POST"])
def yuangongchaxun():
    datas = paixu_yuangong()
    return render_template("员工信息.html", datas=datas)

#仓库信息
def paixu_cangku():
    conn1 = conn()
    sql="""
    select * from cangkuxinxi
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_cangku(id):
    conn1 = conn()
    #从数据库查询单条数据
    sql = f"""
        select * from cangkuxinxi
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

@app.route('/cangku', methods = ["GET", "POST"])
def cangkuchaxun():
    datas = paixu_cangku()
    return render_template("仓库信息.html", datas=datas)
