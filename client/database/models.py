from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Me(Base):
    __tablename__ = 'me'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)

    def __init__(self, id, login):
        self.id = id
        self.login = login


class ContactList(Base):
    __tablename__ = 'contact_list'
    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, unique=True, index=True)
    login = Column(String, unique=True)

    def __init__(self, contact_id, login):
        self.contact_id = contact_id
        self.login = login


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('contact_list.contact_id'))
    to_id = Column(Integer, ForeignKey('contact_list.contact_id'))
    time = Column(String)
    content = Column(String)

    def __init__(self, from_id, to_id, time, content):
        self.from_id = from_id
        self.to_id = to_id
        self.time = time
        self.content = content


Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
