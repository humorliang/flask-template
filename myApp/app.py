# coding:utf-8
"""the app module , containing the app factory function"""
from flask import Flask, render_template, request
from myApp.blue_modules.user import views as user_view
from .extends import db, login_manager, migrate, cache, logInfo, MigrateCommand
from flask_script import Manager


def create_app(config_object='myApp.settings'):
    '''
    app 创建工厂函数
    :param config_object:
    配置对象
    :return:
     flask app
    '''
    app = Flask(__name__)  # __name__代表文件模块名
    print('create app:', app)
    # app.config.from_object('yourapplication.default_config')
    # from yourapplication import default_config
    app.config.from_object(config_object)  # 配置环境变量
    register_blueprints(app)  # 注册蓝图
    register_extents(app)  # 注册扩展
    register_errorhandlers(app)  # 注册错误句柄
    register_command(app)
    return app


def register_blueprints(app):
    '''
    注册蓝图
    :param app:
    app对象
    :return:
    None
    '''
    app.register_blueprint(user_view.blueprint)

    return None


def register_extents(app):
    '''
    扩展初始化
    :param app:
    flask app 对象
    :return:
    None
    '''
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cache.init_app(app)
    logInfo.init_app(app)
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        # logInfo.logger.error(str(error) + ':' + str(request.url))
        logInfo.get_logger('error').error(error_code)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_command(app):
    '''
    注册命令
    db命令：
    flask db init
    flask db migrate
    flask db upgrade
    '''
    manage = Manager(app)  # 初始化管理器
    # 倒入需要迁移的数据模型
    from myApp.data.user.models import User,Address
    manage.add_command('db', MigrateCommand)
