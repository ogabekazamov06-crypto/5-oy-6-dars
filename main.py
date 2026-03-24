from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn

from schemas import (
                    CategoryCreate, CategoryResponse,
                    NewCreate, NewResponse)

from database import get_db, engine, Base
import crud

app = FastAPI()


# 🔹 DB init
async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup_event():
    await init_db()



@app.post('/category/', response_model=CategoryResponse)
async def create_category_endpoint(
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_category(category, db)


@app.get('/category/', response_model=list[CategoryResponse])
async def get_categories_endpoint(db: AsyncSession = Depends(get_db)):
    return await crud.get_categories(db)


@app.get('/category/{category_id}', response_model=CategoryResponse)
async def get_one_category_endpoint(category_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_one_category(category_id, db)


@app.put('/category/{category_id}', response_model=CategoryResponse)
async def update_category_endpoint(
    category_id: int,
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_category(category_id, category, db)


@app.delete('/category/{category_id}')
async def delete_category_endpoint(category_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_category(category_id, db)



@app.post('/news/', response_model=NewResponse)
async def create_news_endpoint(
    news: NewCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_news(news, db)


@app.get('/news/', response_model=list[NewResponse])
async def get_news_endpoint(db: AsyncSession = Depends(get_db)):
    return await crud.get_news(db)


@app.get('/news/{news_id}', response_model=NewResponse)
async def get_one_news_endpoint(news_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_one_news(news_id, db)


@app.put('/news/{news_id}', response_model=NewResponse)
async def update_news_endpoint(
    news_id: int,
    news: NewCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_news(news_id, news, db)


@app.delete('/news/{news_id}')
async def delete_news_endpoint(news_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_news(news_id, db)



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)