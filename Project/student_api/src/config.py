# src/config.py

import os
import mysql.connector as mariadb

class Development(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    #JWT_SECRET_KEY = 'MyFirstRestAPI'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:test@mariadb2:3306/CRUD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    #JWT_SECRET_KEY = 'MyFirstRestAPI'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:test@mariadb2:3306/CRUD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config= {
    'development':Development,
    'production' :Production
}
