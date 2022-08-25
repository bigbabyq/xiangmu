from dataclasses import dataclass
from flask import Flask
from flask import request, render_template, redirect, url_for, session, g

app = Flask(__name__, static_url_path="/")
app.config['SECRET_KEY'] = "sdfklas0lk42j"


@dataclass
class User:
    id: int
    username: str
    password: str


users1 = [
    User(1, "Admin", "123456"),
]
users2 = [

    User(1, "Eason", "888888"),

]


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user1 = [u for u in users1 if u.id == session['user_id']][0]
        user2 = [u for u in users2 if u.id == session['user_id']][0]
        g.user1 = user1
        g.user2 = user2


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 登录操作
        session.pop('user_id', None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        user1 = [u for u in users1 if u.username == username]
        if len(user1) > 0:
            user = user1[0]
        if user1 and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile1'))

    if request.method == 'POST':
        # 登录操作
        session.pop('user_id', None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        user2 = [u for u in users2 if u.username == username]
        if len(user2) > 0:
            user = user2[0]
        if user2 and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile2'))

    return render_template("login.html")


@app.route("/profile1")
def profile1():
    if not g.user1:
        return redirect(url_for('login'))

    return render_template("1.html")

@app.route("/profile2")
def profile2():
    if not g.user2:
        return redirect(url_for('login'))

    return render_template("2.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for('login'))
