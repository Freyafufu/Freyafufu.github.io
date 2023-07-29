# 此文档用来配置数据库信息、连接数据库
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的地址 ‘mysql://用户名:密码@主机名/ip地址:端口号/数据库名’
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/test'

# 跟踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True


# 创建数据库对象
db = SQLAlchemy(app)

# 学生
class Students(db.Model):
    # 定义表名
    __tablename__ = 'students'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    balance = db.Column(db.String(16))
    # photoid = db.Column(db.Integer)
    photo = db.Column(db.BLOB)

# class Photos(db.Model):
#     __tablename__ = 'photos'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True)
#     imgdata = db.Column(db.BLOB)



with app.app_context():
    db.create_all()







