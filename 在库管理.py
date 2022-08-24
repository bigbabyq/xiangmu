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

#盘点单
#在库管理
@app.route('/')
def zaiku():
    return render_template('在库管理.html')

#排序,修改数据库的信息
def paixu_pandiandan():
    conn1 = conn()
    sql="""
    select * from pandiandan
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_pandiandan(id):
    #从数据库查询单条数据
    conn1 = conn()
    sql = f"""
        select * from pandiandan
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

def insert_pandiandan(xuhao,chanpinmingcheng,chanpinguige,zhangmianshuliang,shicunshuliang,chazhi,baozhiqi,daoqiri,beizhu):
    #新增数据到mysql
    conn1 = conn()
    sql =f"""
       insert into pandiandan
       (xuhao,chanpinmingcheng,chanpinguige,zhangmianshuliang,shicunshuliang,chazhi,baozhiqi,daoqiri,beizhu)
       values('{xuhao}','{chanpinmingcheng}','{chanpinguige}','{zhangmianshuliang}','{shicunshuliang}','{chazhi}','{baozhiqi}','{daoqiri}','{beizhu}')
       """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def delete_pandiandan(id):
    #删除数据库id的记录
    conn1 = conn()
    sql = f"""
        delete from pandiandan
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def update_pandiandan(id,xuhao,chanpinmingcheng,chanpinguige,zhangmianshuliang,shicunshuliang,chazhi,baozhiqi,daoqiri,beizhu):
    #修改数据
    conn1 = conn()
    sql = f"""
        update pandiandan
        set xuhao='{xuhao}',chanpinmingcheng='{chanpinmingcheng}',chanpinguige='{chanpinguige}',zhangmianshuliang='{zhangmianshuliang}',shicunshuliang='{shicunshuliang}',chazhi='{chazhi}',baozhiqi='{baozhiqi}',daoqiri='{daoqiri}',beizhu='{beizhu}'
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

#删除数据
@app.route("/delete_pandiandan", methods=["GET"])
def delete_pandian():
    id = request.args.get("id")
    delete_pandiandan(id)
    return redirect("/pandiandan")

#修改数据
@app.route("/盘点单修改", methods=["GET", "POST"])
def edit_pandiandan():
    id = request.args.get("id")
    data = select_pandiandan(id)
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        chanpinmingcheng = request.form.get("chanpinmingcheng")
        chanpinguige = request.form.get("chanpinguige")
        zhangmianshuliang = request.form.get("zhangmianshuliang")
        shicunshuliang = request.form.get("shicunshuliang")
        chazhi = request.form.get("chazhi")
        baozhiqi = request.form.get("baozhiqi")
        daoqiri = request.form.get("daoqiri")
        beizhu = request.form.get("beizhu")
        update_pandiandan(id,xuhao, chanpinmingcheng, chanpinguige, zhangmianshuliang, shicunshuliang,chazhi,baozhiqi,daoqiri,beizhu)
        return redirect("/pandiandan")

    return render_template("盘点单修改.html", data=data)

#增加数据
@app.route('/pandiandan', methods=["GET","POST"])
def index_pandiandan():
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        chanpinmingcheng = request.form.get("chanpinmingcheng")
        chanpinguige = request.form.get("chanpinguige")
        zhangmianshuliang = request.form.get("zhangmianshuliang")
        shicunshuliang = request.form.get("shicunshuliang")
        chazhi = request.form.get("chazhi")
        baozhiqi = request.form.get("baozhiqi")
        daoqiri = request.form.get("daoqiri")
        beizhu = request.form.get("beizhu")
        insert_pandiandan(xuhao, chanpinmingcheng, chanpinguige, zhangmianshuliang, shicunshuliang,chazhi,baozhiqi,daoqiri,beizhu)
    datas=paixu_pandiandan()
    return render_template("生成盘点单.html", datas=datas)

@app.route('/生成盘点单', methods = ["GET", "POST"])
def pandiandanchaxun():
    datas = paixu_pandiandan()
    return render_template("生成盘点单.html", datas=datas)

#缺货单

def paixu_quehuodan():
    conn1 = conn()
    sql="""
    select * from quehuodan
    order by id asc
    """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()

def select_quehuodan(id):
    #从数据库查询单条数据
    conn1 = conn()
    sql = f"""
        select * from quehuodan
        where id = {id}
        """
    cursor = conn1.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()

def insert_quehuodan(xuhao,chanpinmingcheng,guige,danwei,quehuoshuliang,danjia,zuidichuliang,suoxuzijin,beizhu):
    #新增数据到mysql
    conn1 = conn()
    sql =f"""
       insert into quehuodan
       (xuhao,chanpinmingcheng,guige,danwei,quehuoshuliang,danjia,zuidichuliang,suoxuzijin,beizhu)
       values('{xuhao}','{chanpinmingcheng}','{guige}','{danwei}','{quehuoshuliang}','{danjia}','{zuidichuliang}','{suoxuzijin}','{beizhu}')
       """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def delete_quehuodan(id):
    #删除数据库id的记录
    conn1 = conn()
    sql = f"""
        delete from quehuodan
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

def update_quehuodan(id,xuhao,chanpinmingcheng,guige,danwei,quehuoshuliang,danjia,zuidichuliang,suoxuzijin,beizhu):
    #修改数据
    conn1 = conn()
    sql = f"""
        update quehuodan
        set xuhao='{xuhao}',chanpinmingcheng='{chanpinmingcheng}',guige='{guige}',danwei='{danwei}',quehuoshuliang='{quehuoshuliang}',danjia='{danjia}',zuidichuliang='{zuidichuliang}',suoxuzijin='{suoxuzijin}',beizhu='{beizhu}'
        where id={id}
        """
    cursor = conn1.cursor()
    cursor.execute(sql)
    conn1.commit()

#删除数据
@app.route("/delete_quehuodan", methods=["GET"])
def delete_quehuo():
    id = request.args.get("id")
    delete_quehuodan(id)
    return redirect("/quehuodan")

#修改数据
@app.route("/缺货单修改", methods=["GET", "POST"])
def edit_quehuodan():
    id = request.args.get("id")
    data = select_quehuodan(id)
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        chanpinmingcheng = request.form.get("chanpinmingcheng")
        guige = request.form.get("guige")
        danwei = request.form.get("danwei")
        quehuoshuliang = request.form.get("quehuoshuliang")
        danjia = request.form.get("danjia")
        zuidichuliang = request.form.get("zuidichuliang")
        suoxuzijin = request.form.get("suoxuzijin")
        beizhu = request.form.get("beizhu")
        update_quehuodan(id,xuhao,chanpinmingcheng,guige,danwei,quehuoshuliang,danjia,zuidichuliang,suoxuzijin,beizhu)
        return redirect("/quehuodan")

    return render_template("缺货单修改.html", data=data)

#增加数据
@app.route('/quehuodan', methods=["GET","POST"])
def index_quehuodan():
    if request.method == "POST":
        xuhao = request.form.get("xuhao")
        chanpinmingcheng = request.form.get("chanpinmingcheng")
        guige = request.form.get("guige")
        danwei = request.form.get("danwei")
        quehuoshuliang = request.form.get("quehuoshuliang")
        danjia = request.form.get("danjia")
        zuidichuliang = request.form.get("zuidichuliang")
        suoxuzijin = request.form.get("suoxuzijin")
        beizhu = request.form.get("beizhu")
        insert_quehuodan(xuhao,chanpinmingcheng,guige,danwei,quehuoshuliang,danjia,zuidichuliang,suoxuzijin,beizhu)
    datas=paixu_quehuodan()
    return render_template("生成缺货单.html", datas=datas)

@app.route('/生成缺货单', methods = ["GET", "POST"])
def quehuodanchaxun():
    datas = paixu_quehuodan()
    return render_template("生成缺货单.html", datas=datas)

if __name__ == "__main__":
    app.run(debug=True)
