# coding:utf-8
'''数据库封装,独立db对象,防止循环引入'''
from .extends import db

Column = db.Column  # 数据库字段
relationship = db.relationship  # 外健


class CRUDMixin(object):
    '''
    mixin CRUD(create,read,update,delete)
    '''

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)  # 实例化一个类对象
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class SurrogatePK(object):
    """A mixin that adds a surrogate(替代) integer 'primary key' column named ``id`` to any declarative-mapped class.
    创建一个id字段并且为主健
    """

    __table_args__ = {'extend_existing': True}

    id = Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def get_by_id(cls, record_id):
        """
        Get record by ID.
        any(iterable):可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True
        S.isdigit()：是否由数字组成
        """
        if any(
                (isinstance(record_id, (str, bytes)) and record_id.isdigit(),
                 isinstance(record_id, (int, float))),
        ):
            return cls.query.get(int(record_id))
        return None


class Model(CRUDMixin, SurrogatePK, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True


# 外健示例一对多：A---1-n-->B 外健设立在多的一方,关系也在多的一方
'''
# SQLAlchemy关系模型
class A(db.Model):
    __tablename__='a'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))

class B(db.Model):
    __tablename__='b'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    # 设置外健
    a_id=db.Column(db.Integer,db.ForeginKey('a.id')) # a表名
    # 关系对象
    a=db.relationship('A',backref=db.backref('b',lazy='dynamic')) # 对象名 表名
    
    >>> aInstance = A(name='aname')
    >>> B(name='bname', a=aInstance)
'''


def reference_col(tablename, nullable=False, pk_name='id', **kwargs):
    """
    参考列：添加一个外健字段
    Column that adds primary key foreign key reference.
    Usage: ::
        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    return Column(
        db.ForeignKey('{0}.{1}'.format(tablename, pk_name)),
        nullable=nullable, **kwargs)
