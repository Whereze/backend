from sqlalchemy import Column, Integer, String

from service.models.db import Base, engine


class waterfall(Base):
    __tablename__ = 'waterfalls'

    uid = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())
    height = Column(Integer())
    size = Column(Integer())

    def __repr__(self):
        return f'Waterfall {self.uid}, {self.title}'


class waterfall_details(Base):
    __tablename__ = 'waterfalls_details'

    uid = Column(Integer, primary_key=True)
    title = Column(String())
    url = Column(String())
    summary = Column(String())
    height = Column(String())
    width = Column(String())
    river = Column(String())
    country = Column(String())
    region = Column(String())
    RF_subject = Column(String())

    def __repr__(self):
        return f'Waterfall_Details {self.uid}, {self.title}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
