import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_database:str = 'database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f'sqlite:///{os.path.join(base_dir, sqlite_database)}'

Engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=Engine)
Base = declarative_base()