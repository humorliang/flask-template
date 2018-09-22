# coding:utf-8
# environs管理环境变量模块
from environs import Env

# 创建环境变量
env = Env()

# 读取环境变量
env.read_env()  # .env文件

# mysql数据库设置
# HOSTNAME = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'cardcms'
# USERNAME = 'root'
# PASSWORD = '123456'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(env.str("DBUSERNAME"), env.str("PASSWORD"),
                                                              env.str("HOSTNAME"), env.str("PORT"),
                                                              env.str("DATABASE"))

# 设置flask中的全局变量：全为大写字母
ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = DB_URL
SECRET_KEY = env.str('SECRET_KEY')
CACHE_TYPE = env.str('CACHE_TYPE')
SQLALCHEMY_TRACK_MODIFICATIONS = env.str('SQLALCHEMY_TRACK_MODIFICATIONS')
