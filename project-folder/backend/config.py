import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secure_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:9881470992@localhost/PostgreSQL 16'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
