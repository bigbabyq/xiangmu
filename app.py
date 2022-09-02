import pymysql
from flask import Flask, render_template
from data import get_loan_number

def get_loan_number():
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user="root",
        passwd="hq261328",
        db="超市仓储管理信息系统",
        charset='utf8'
    )
    print("---读取数据---")
    cursor = db.cursor()  # 使用连接对象获得一个cursor对象
    sql = "select mingcheng,shuliang  from chanpinziliao"
    cursor.execute(sql)  # 用于执行返回多个结果集、多个更新计数或二者组合的语句。
    number = cursor.fetchall()  # 返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
    temp_data = []
    loan_count = 0
    for loanNumber in number:
        loan_count += 1
        temp_data.append(loanNumber)
    data11 = dict(temp_data)
    # print(data11)
    cursor.close()
    db.close()
    print("读取完成,共有%d条数据……" % loan_count)
    return data11

# 引入核心模块

# 通过当前文件构建一个app应用，当前文件就是web和App的入口
app = Flask(__name__)

# 定义视图处理函数加载到App中（路由+视图函数）
@app.route('/') # 访问路由
def hello_world(): # 绑定的视图函数
    temp_data = get_loan_number()
    return render_template('bar-simple.html',map_data=temp_data)

if __name__ == '__main__':
    app.run()
