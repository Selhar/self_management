from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column as Column, Integer, String

Base = declarative_base()

class Cards(Base):
    __tablename__ = "cards"    

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
    age = Column(Integer)