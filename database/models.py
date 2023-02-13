import datetime

from sqlalchemy import create_engine, Column, BigInteger, Text, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine("sqlite:///database/database.db")
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger)
    username = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    register_date = Column(DateTime, default=datetime.datetime.now().replace(microsecond=0))
