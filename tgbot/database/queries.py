from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from ..database.models import User

engine = create_async_engine("sqlite+aiosqlite:///database.db")
session_factory = async_sessionmaker(bind=engine)


async def add_user(user):
    async with session_factory() as session:
        new_user = User(**user)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


async def get_user(user_id: int):
    async with session_factory() as session:
        row = await session.execute(select(User).filter_by(user_id=user_id))
        return row.scalar_one_or_none()


async def get_users():
    async with session_factory() as session:
        row = await session.execute(select(User))
        return row.scalars().all()


async def edit_user(user_id: int, obj_data_dict: dict):
    async with session_factory() as session:
        stmt = update(User).values(**obj_data_dict).filter_by(user_id=user_id)
        obj = await session.execute(stmt)
        await session.commit()
