# conding:utf-8
'''flask扩展模块：进行扩展创建 然后在工厂函数中进行初始化'''
from flask_sqlalchemy import SQLAlchemy  # 数据库
from flask_caching import Cache  # 缓存
from flask_login import LoginManager  # 登陆管理器
from flask_migrate import Migrate, MigrateCommand  # 数据迁移
from myApp.tools.LogConfig import LogInfo  # 日志信息

# 扩展对象创建
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
cache = Cache()
logInfo = LogInfo()
