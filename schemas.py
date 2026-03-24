from pydantic import BaseModel

class CategoryCreate(BaseModel):

    name: str


class CategoryResponse(CategoryCreate):
    id: int

    class Config:
        from_attributes = True


class NewCreate(BaseModel):
    name: str
    price:int
    author: str
    category_id: int

class NewResponse(NewCreate):
    id: int
    class Config:
        from_attributes = True