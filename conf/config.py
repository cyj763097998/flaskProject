#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

#mysql
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '10.4.19.200'
PORT = '3306'
DATABASE = 'news'
#连接
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,
	HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False