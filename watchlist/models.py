import datetime

from watchlist import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

# 创建数据库模型类
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True) # 主键
    name = db.Column(db.String(20)) 
    username = db.Column(db.String(20))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)


class Ariticles(db.Model):
    id = db.Column(db.Integer,primary_key=True) # 主键
    title = db.Column(db.String(50))#标题
    content = db.Column(db.Text)#内容
    author = db.Column(db.String(20))#作者

    pubdate = db.Column(db.String(30),index=True, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))#发布时间