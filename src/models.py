import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Follower(Base):
     __tablename__ = 'follower'
     id = Column(Integer, primary_key=True)
     user_from_id = Column(Integer, ForeignKey('user.id'))
     user_to_id = Column(Integer, ForeignKey('user.id'))


class Post(Base):
     __tablename__ = 'post'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     user = relationship(User)

class Media(Base):
     __tablename__ = 'media'
     id = Column(Integer, primary_key=True)
     url = Column(String(250), nullable=False)
     post_id = Column(Integer, ForeignKey('post.id'))
     post = relationship(Post)

class Comment(Base):
     __tablename__ = 'comment'
     id = Column(Integer, primary_key=True)
     comment_test = Column(String(1000), nullable=False)
     author_id = Column(Integer, ForeignKey('user.id'))
     user = relationship(User)
     post_id = Column(Integer, ForeignKey('post.id'))
     post = relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
