# coding:utf-8
'''用户数据模型'''
from myApp.extends import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))
    address = db.relationship('Address', backref='user', lazy=True)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
