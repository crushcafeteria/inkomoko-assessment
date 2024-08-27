from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DB_URL = "sqlite:///./sql_app.db"
DB_URL = "mariadb+pymysql://root:root@127.0.0.1:33060/inkomoko?charset=utf8mb4"


engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
