from src.models.base_class import Base
from sqlalchemy import Column as SQLColumn, Integer, String

class Columns(Base):
    __tablename__ = "columns"    

    id = SQLColumn(Integer, primary_key=True, index=True)
    title = SQLColumn(String, nullable=False)
    position = SQLColumn(Integer, nullable=False, unique=True)