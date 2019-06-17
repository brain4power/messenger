from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

engine = create_engine('sqlite:///server.sqlite')
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    information = Column(String)

    def __init__(self, login, information=''):
        self.login = login
        self.information = information

    @classmethod
    def get_user_id_by_login(cls, session, login):
        return session.query(cls).filter(cls.login == login).one()

    @classmethod
    def get_all_users(cls, session):
        data = session.query(cls).all()
        return data

    def __repr__(self):
        return '{}'.format(self.login)


class UserContact(Base):
    __tablename__ = 'user_contact'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    contact_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, owner_id, contact_id):
        self.owner_id = owner_id
        self.contact_id = contact_id

    @classmethod
    def get_user_contacts(cls, session, owner_id):
        return session.query(cls.contact_id).filter(cls.owner_id == owner_id).one()

    @classmethod
    def add_contact(cls, session, owner_id, contact_id):
        session.add(UserContact(owner_id, contact_id))

    @classmethod
    def del_contact(cls, session, owner_id, contact_id):
        obj = session.query(cls.contact_id).filter(cls.owner_id == owner_id and contact_id == contact_id).one()
        session.delete(obj)


class UserHistory(Base):
    __tablename__ = 'user_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    enter_time = Column(Integer)
    ip_address = Column(String)

    def __init__(self, user_id, ip_adress):
        self.user_id = user_id
        self.ip_address = ip_adress
        self.enter_time = datetime.now()


Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
