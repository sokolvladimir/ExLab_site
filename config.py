import os
from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

DATABASE = {
    'drivername': 'postgresql+asyncpg',
    'host': os.environ.get('POSTGRES_HOST', 'localhost'),
    'port': os.environ.get('POSTGRES_PORT', '5433'),
    'username': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'database': os.environ.get('POSTGRES_NAME', 'postgres')
}

DATABASE_ALEMBIC = f"postgresql+psycopg2://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:" \
                   f"{DATABASE['port']}/{DATABASE['database']}"

