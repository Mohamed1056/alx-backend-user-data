#!/user/bin/env python3
"""
creating a DOM for database called user.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    User class for connecting to sql
    Its attributes:
    __tablename__ : the name of the table in the
    database.
    id(int): store the id.
    email(str): stores the email.
    hashed_password(str): stores the hashed
    password of the user.
    session_id(str): stores the session id.
    reset_token(str): stores the tokens.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)
