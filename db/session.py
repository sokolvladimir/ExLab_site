from typing import Generator

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import DATABASE

engine = create_async_engine(URL.create(**DATABASE), pool_recycle=3600, echo=True, future=True)

async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> Generator:
    """Dependency for getting a database async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
