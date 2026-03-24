from  sqlalchemy.ext.asyncio import  AsyncSession

from  schemas import  (CategoryResponse,CategoryCreate)

from models import  Category,News

async  def create_category(category: CategoryCreate, db: AsyncSession)-> CategoryResponse:
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return  CategoryResponse.model_validate(db_category)
