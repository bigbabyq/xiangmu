from flask import Flask, render_template, request, redirect
import pymysql

app = Flask("代办项网站")
def conn():
    conn = pymysql.connect(
        host="127.0.0.1",
        user='root',
        password='hq261328',
        port=3306,
        db='超市零食仓储信息系统',
        charset='utf8'
    )
    return conn

#货物状态
@app.route('/')
def huowu():
    return render_template('货物状态.html')

#排序,修改数据库的信息
def paixu_buhuodan():
    conn1 = conn()
    sql="""
    select * from buhuodan
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_buhuodan(id):
    conn1 = conn()
    #从数据库查询单条数据
    sql = f"""
        select * from buhuodan
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

def insert_buhuodan(xuhao, chanpinmingcheng, danwei, shuliang,danjia,zongji,beizhu):
    #新增数据到mysql
    conn1 = conn()
    sql =f"""
       insert into buhuodan
       (xuhao, chanpinmingcheng, danwei, shuliang,danjia,zongji,beizhu)
       values('{xuhao}','{chanpinmingcheng}','{danwei}','{shuliang}','{danjia}','{zongji}','{beizhu}')
       """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def update_buhuodan(id,xuhao, chanpinmingcheng, danwei, shuliang,danjia,zongji,beizhu):
    #更新数据
    conn1 = conn()
    sql = f"""
        update buhuodan
        set xuhao='{xuhao}',chanpinmingcheng='{chanpinmingcheng}',danwei='{danwei}',shuliang='{shuliang}',danjia='{danjia}',zongji='{zongji}',beizhu='{beizhu}'
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def delete_buhuodan(id):
    #删除数据库id的记录
    conn1 = conn()
    sql = f"""
        delete from buhuodan
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

@app.route("/delete_buhuodan", methods=["GET"])
def delete_buhuodan():
    id = request.args.get("id")
    delete_buhuodan(id)
    return redirect("/buhuodan")

@app.route("/补货单修改", methods=["GET", "POST"])
def edit_buhuodan():
    id = request.args.get("id")
    data = select_buhuodan(id)
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        chanpinmingcheng = request.form.get("chanpinmingcheng")
        danwei = request.form.get("danwei")
        shuliang = request.form.get("shuliang")
        danjia = request.form.get("danjia")
        zongji = request.form.get("zongji")
        beizhu = request.form.get("beizhu")
        update_buhuodan(id,xuhao, chanpinmingcheng, danwei, shuliang,danjia,zongji,beizhu)
        return redirect("/buhuodan")

    return render_template("补货单修改.html", data=data)

@app.route('/buhuodan', methods=["GET","POST"])
def index_buhuodan():
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        chanpinmingcheng = request.form.get("chanpinmingcheng")
        danwei = request.form.get("danwei")
        shuliang = request.form.get("shuliang")
        danjia = request.form.get("danjia")
        zongji = request.form.get("zongji")
        beizhu = request.form.get("beizhu")
        insert_buhuodan(xuhao, chanpinmingcheng,danwei, shuliang,danjia,zongji,beizhu)
    datas=paixu_buhuodan()
    return render_template("生成补货单.html", datas=datas)

@app.route('/生成补货单', methods = ["GET", "POST"])
def shengchengbuhuodan():
    datas = paixu_buhuodan()
    return render_template("生成补货单.html", datas=datas)
app.run(debug=True)