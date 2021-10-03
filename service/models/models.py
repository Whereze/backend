from sqlalchemy import Column, Integer, String

from db import Base, engine

class waterfall(Base):
    __tablename__ = 'waterfalls'

    uid = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())
    height = Column(Integer())
    size = Column(Integer())

    def __repr__(self):
        return f'Waterfall {self.uid}, {self.title}'

if __name__ == '__main__':
    Base.metadata.create_all(engine)