from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column as SQLColumn, Integer, String

Base = declarative_base()

class Columns(Base):
    __tablename__ = "columns"    

    id = SQLColumn(Integer, primary_key=True, index=True)
    title = SQLColumn(String, nullable=False)
    position = SQLColumn(Integer, nullable=False, unique=True)
    age = SQLColumn(Integer)