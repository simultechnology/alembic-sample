from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'

    ID = Column(Integer, primary_key=True)
    Name = Column(String(35), nullable=False)
    CountryCode = Column(String(3), nullable=False)
    District = Column(String(20), nullable=False)
    Population = Column(Integer, nullable=False)
    # Area = Column(Integer, nullable=True)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)