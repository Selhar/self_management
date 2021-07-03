from pydantic import BaseModel

class Columns(BaseModel):
    id: int
    title: str = None
    position: int
    
    class Config:
        orm_mode = True