import pymysql
import os
class Config:
    db_url = os.environ.get("DATABASE_URL")

    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    SECRET_KEY = "secret-key"
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
