#encoding: utf-8
from exts import db
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    salt = db.Column(db.String(30), nullable=False)
    avatar = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    loginfailure = db.Column(db.SmallInteger, nullable=False)
    logintime = db.Column(db.Integer, nullable=False)
    createtime = db.Column(db.Integer, nullable=False)
    updatetime = db.Column(db.Integer, nullable=False)
    token = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    pid = db.Column(db.Integer,nullable=False)
    name = db.Column(db.String(100), nullable=False)
    rules = db.Column(db.Text, nullable=False)
    createtime = db.Column(db.Integer, nullable=False)
    updatetime = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(30), nullable=False)
class Rule(db.Model):
    __tablename__ = "rule"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    type = db.Column(db.Enum("file","menu"), nullable=False)
    pid = db.Column(db.Integer, nullable=False,index=True,default=0)
    name = db.Column(db.String(100),unique=True,nullable=False)
    title = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(255), nullable=False)
    remark = db.Column(db.String(255), nullable=False)
    ismenu = db.Column(db.SmallInteger, nullable=False)
    createtime = db.Column(db.Integer, nullable=False)
    updatetime = db.Column(db.Integer, nullable=False)
    weigh = db.Column(db.Integer, nullable=False,index=True,default=0)
    status = db.Column(db.String(30), nullable=False)
