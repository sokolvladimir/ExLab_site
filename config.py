import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ.get('POSTGRES_HOST', 'localhost'),
    'port': os.environ.get('POSTGRES_PORT', '5432'),
    'username': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'database': os.environ.get('POSTGRES_NAME', 'exlab_test')
}


engine = create_async_engine(URL.create(**DATABASE), pool_recycle=3600, echo=True, future=True)

async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
