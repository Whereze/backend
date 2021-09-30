from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://whereze:whereze@localhost:5432/whereze')
db_session = scoped_session(sessionmaker(bing=engine))

Base = declarative_base()
Base.query = db_session.query_property()