# coding:utf-8
'''user view and router and create user blueprint'''
from flask import Blueprint, request
from myApp.extends import logInfo

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../../static')


@blueprint.route('/')
def members():
    '''
    成员函数
    :return:
    '''

    return str(request.base_url)
