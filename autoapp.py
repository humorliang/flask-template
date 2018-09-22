# coding:utf-8

# 创建一个app实例
from myApp.app import create_app

'''start app need export sys path for $ export FLASK_APP=hello.py'''
'''linux export can add or update sys path .$ export -p //show all sys path'''
app = create_app()
