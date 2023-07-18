from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:passw0rd1!@192.168.1.100:15432/fastapi"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:passw0rd@192.168.1.10/fastapi"

#actual database session
#session local(db session) vs session (sqlalchemy)
engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # only for SQLite
    SQLALCHEMY_DATABASE_URL # for postgres

)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# later imported from model
# returns a class
Base = declarative_base()
