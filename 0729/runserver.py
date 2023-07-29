import MySQLdb
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import config


app = config.app
db = config.db

# 主页面
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('file.html')


@app.route('/upload', methods=['POST'])
def upload():
    # upload_file = request.files.get('file')
    # print(upload_file)
    mydict = config.Students(id=request.form["id"], name=request.form["name"], balance=request.form["balance"], photo=request.form["photo"])
    with app.app_context():
        db.session.add_all(mydict)
        db.session.commit()
    return "sucessful"

@app.route('/show', methods=['GET'])
def show():
    # cursor = db.cursor()
    cursor = db.cursor(MySQLdb.cursors.DictCursor)  # 定义一个游标
    cursor.execute("select * from Students")  # sql语句
    datas = cursor.fetchall()  # 获取数据

    return render_template('data.html', mycol=datas)


if __name__ == '__main__':
    app.run(debug=True)
