from pydantic import BaseModel

class Cards(BaseModel):
    id: int
    text: str
    position: int
    column_id: int    
    
    class Config:
        orm_mode = True