from flask import Flask, render_template, request, redirect
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

#入库管理
@app.route('/')
def ruku():
    return render_template('入库管理.html')

#排序,修改数据库的信息
def paixu_rukudan():
    conn1 = conn()
    sql="""
    select * from rukudan
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_rukudan(id):
    conn1 = conn()
    #从数据库查询单条数据
    sql = f"""
        select * from rukudan
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

def insert_rukudan(xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu):
    #新增数据到mysql
    conn1 = conn()
    sql =f"""
       insert into rukudan
       (xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu)
       values('{xuhao}','{mingcheng}','{guige}','{danwei}','{shuliang}','{danjia}','{jine}','{beizhu}')
       """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def update_rukudan(id,xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu):
    #更新数据
    conn1 = conn()
    sql = f"""
        update rukudan
        set xuhao='{xuhao}',mingcheng='{mingcheng}',guige='{guige}',danwei='{danwei}',shuliang='{shuliang}',danjia='{danjia}',jine='{jine}',beizhu='{beizhu}'
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def delete_rukudan(id):
    #删除数据库id的记录
    conn1 = conn()
    sql = f"""
        delete from rukudan
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

@app.route("/delete_rukudan", methods=["GET"])
def delete_ruku():
    id = request.args.get("id")
    delete_rukudan(id)
    return redirect("/rukudan")

@app.route("/入库单修改", methods=["GET", "POST"])
def edit_rukudan():
    id = request.args.get("id")
    data = select_rukudan(id)
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        mingcheng = request.form.get("mingcheng")
        guige = request.form.get("guige")
        danwei = request.form.get("danwei")
        shuliang = request.form.get("shuliang")
        danjia = request.form.get("danjia")
        jine = request.form.get("jine")
        beizhu = request.form.get("beizhu")
        update_rukudan(id,xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu)
        return redirect("/rukudan")

    return render_template("入库单修改.html", data=data)

@app.route('/rukudan', methods=["GET","POST"])
def index_rukudan():
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        mingcheng = request.form.get("mingcheng")
        guige = request.form.get("guige")
        danwei = request.form.get("danwei")
        shuliang = request.form.get("shuliang")
        danjia = request.form.get("danjia")
        jine = request.form.get("jine")
        beizhu = request.form.get("beizhu")
        insert_rukudan(xuhao, mingcheng, guige, danwei, shuliang,danjia,jine,beizhu)
    datas=paixu_rukudan()
    return render_template("生成入库单.html", datas=datas)

@app.route('/生成入库单', methods = ["GET", "POST"])
def rukudanchaxun():
    datas = paixu_rukudan()
    return render_template("生成入库单.html", datas=datas)
app.run(debug=True)