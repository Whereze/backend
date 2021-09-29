from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine()
db_session = declarative_base()

Base = declarative_base()
Base.query = db_session.query_property()