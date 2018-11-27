#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from run import app
from exts import db
from models import Admin,Role,Rule

manager = Manager(app)

#使用Migrate绑定app,db
migrate = Migrate(app,db)

#添加迁移脚本的命令
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
	manager.run()