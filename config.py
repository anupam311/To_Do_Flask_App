import pymysql

class Config:
    SECRET_KEY = "secret-key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://sarthak:sarthak114942@localhost:3306/to_do_app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False