import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Float

from scrappy import db


class Store(db.Model):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)
    url = Column(String(500))
    active = Column(Boolean(), default=True)
    articles = db.relationship('Article', backref='store', lazy=True)

    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url

    def __repr__(self):
        return "<Store(id=%d, name='%s', url='%s', active='%d')>" % (self.id, self.name, self.url, self.active)

    def __to_dict__(self):
        return {'id': self.id, 'name': self.name, 'url': self.url, 'active': self.active}


class Article(db.Model):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    oid = Column(String(100), unique=True, nullable=False)
    name = Column(String(1000))
    brand = Column(String(1000))
    url = Column(String(1000))
    category = Column(String(1000))
    create_date = Column(DateTime, default=datetime.datetime.utcnow())
    description = Column(Text)
    prices = db.relationship('Price', backref='article', lazy=True)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)

    def __init__(self, oid=None, brand=None, name=None, url=None, category=None, create_date=None, description=None,
                 store_id=None):
        self.oid = oid
        self.name = name
        self.brand = brand
        self.url = url
        self.category = category
        self.create_date = create_date
        self.description = description
        self.store_id = store_id

    def __repr__(self):
        return "<Article(id=%d, oid='%s', brand='%s', url='%s', name='%s', category='%s', create_date='%s', " \
               "description='%s', store_id='%d')>" % (self.id, self.oid, self.brand, self.url, self.name, self.category,
                                                      self.create_date, self.description, self.store_id)

    def __to_dict__(self):
        return {'id': self.id, 'oid': self.oid, 'brand': self.brand, 'url': self.url, 'name': self.name,
                'category': self.category, 'create_date': self.create_date, 'description': self.description,
                'store_id': self.store_id}


class Price(db.Model):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, default=0.0)
    discount = Column(Float, default=0.0)
    discount_desc = Column(String(100))
    discount_code = Column(String(100))
    date = Column(DateTime, default=datetime.datetime.utcnow())
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)

    def __init__(self, value=None, discount=None, discount_desc=None, discount_code=None, date=None, article_id=None):
        self.value = value
        self.discount = discount
        self.discount_desc = discount_desc
        self.discount_code = discount_code
        self.date = date
        self.article_id = article_id

    def __repr__(self):
        return "<Price(id=%d, value='%d', discount='%d', discount_desc='%d', discount_code='%s', date='%s', " \
               "article_id='%s')>" % (self.id, self.value, self.discount, self.discount_desc, self.discount_code,
                                      self.date, self.article_id)

    def __to_dict__(self):
        return {'id': self.id, 'value': self.value, 'discount': self.discount, 'discount_desc': self.discount_desc,
                'discount_code': self.discount_code, 'date': self.date}
