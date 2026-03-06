# app/models.py

from app import db # to bring SQLAlchemy instance (db) from __init__.py to this module so we can define our database models here

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # to define the primary key for the user
    username = db.Column(db.VARCHAR(150), unique=True, nullable=False) # to define the username of the user, which must be unique and cannot be null
    password = db.Column(db.VARCHAR(255), nullable=False) # to define the password of the user, which cannot be null

    tasks = db.relationship(
        'Task', 
        backref='user',  
        cascade="all, delete-orphan",
        passive_deletes=True
    )

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # to define the primary key for the task
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE")) # to define a foreign key relationship with the User model, so that when a user is deleted, all their tasks are also deleted
    title = db.Column(db.String(100), nullable=False) # to define the title of the task, which cannot be null
    description = db.Column(db.Text, nullable=True) # to define the description of the task, which can be null
    status = db.Column(db.String(20), default="pending") # to define whether the task is completed or not, with a default value of "pending"

