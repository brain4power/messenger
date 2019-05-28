from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

engine = create_engine('sqlite:///server.sqlite', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    information = Column(String)

    def __init__(self, login, information=''):
        self.login = login
        self.information = information


class UserContact(Base):
    __tablename__ = 'user_contact'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey(User.__tablename__.join('.id')))
    contact_id = Column(Integer, ForeignKey(User.__tablename__.join('.id')))

    def __init__(self, owner_id, contact_id):
        self.owner_id = owner_id
        self.contact_id = contact_id

    def get_user_contacts(self, session, owner_id):
        pass


class UserHistory(Base):
    __tablename__ = 'user_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.__tablename__.join('.id')))
    enter_time = Column(Integer)
    ip_address = Column(String)

    def __init__(self, user_id, ip_adress):
        self.user_id = user_id
        self.ip_address = ip_adress
        self.enter_time = datetime.now()
