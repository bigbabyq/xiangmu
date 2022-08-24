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

#出库管理
@app.route('/')
def chuku():
    return render_template('出库管理.html')

#排序,修改数据库的信息
def paixu_chukudan():
    conn1 = conn()
    sql="""
    select * from chukudan
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_chukudan(id):
    #从数据库查询单条数据
    conn1 = conn()
    sql = f"""
        select * from chukudan
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

def insert_chukudan(xuhao,mingcheng,guige,danwei,shuliang,danjia,jine,beizhu):
    #新增数据到mysql
    conn1 = conn()
    sql =f"""
       insert into chukudan
       (xuhao,mingcheng,guige,danwei,shuliang,danjia,jine,beizhu)
       values('{xuhao}','{mingcheng}','{guige}','{danwei}','{shuliang}','{danjia}','{jine}','{beizhu}')
       """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def delete_chukudan(id):
    #删除数据库id的记录
    conn1 = conn()
    sql = f"""
        delete from chukudan
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def update_chukudan(id,xuhao,mingcheng,guige,danwei,shuliang,danjia,jine,beizhu):
    #修改数据
    conn1 = conn()
    sql = f"""
        update chukudan
        set xuhao='{xuhao}',mingcheng='{mingcheng}',guige='{guige}',danwei='{danwei}',shuliang='{shuliang}',danjia='{danjia}',jine='{jine}',beizhu='{beizhu}'
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

#删除数据
@app.route("/delete_chukudan", methods=["GET"])
def delete_chuku():
    id = request.args.get("id")
    delete_chukudan(id)
    return redirect("/chukudan")

#修改数据
@app.route("/出库单修改", methods=["GET", "POST"])
def edit_chukudan():
    id = request.args.get("id")
    data = select_chukudan(id)
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        mingcheng = request.form.get("mingcheng")
        guige = request.form.get("guige")
        danwei = request.form.get("danwei")
        shuliang = request.form.get("shuliang")
        danjia = request.form.get("danjia")
        jine = request.form.get("jine")
        beizhu = request.form.get("beizhu")
        update_chukudan(id,xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu)
        return redirect("/chukudan")

    return render_template("出库单修改.html", data=data)

#增加数据
@app.route('/chukudan', methods=["GET","POST"])
def index_chukudan():
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        mingcheng = request.form.get("mingcheng")
        guige = request.form.get("guige")
        danwei = request.form.get("danwei")
        shuliang = request.form.get("shuliang")
        danjia = request.form.get("danjia")
        jine = request.form.get("jine")
        beizhu = request.form.get("beizhu")
        insert_chukudan(xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu)
    datas=paixu_chukudan()
    return render_template("生成出库单.html", datas=datas)

@app.route('/生成出库单', methods = ["GET", "POST"])
def chukudanchaxun():
    datas = paixu_chukudan()
    return render_template("生成出库单.html", datas=datas)

app.run(debug=True)