from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()                                                                                                       

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:thiago06102006@localhost/projeto_jogo_de_aposta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False