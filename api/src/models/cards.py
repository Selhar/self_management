from src.models.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Cards(Base):
    __tablename__ = "cards"    

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
    column_id = Column(Integer, ForeignKey("columns.id"))