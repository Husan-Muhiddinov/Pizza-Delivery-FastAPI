from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker



engine = create_engine("postgresql+psycopg2://postgres:tiger@localhost/pizza_delivery",
    echo=True
)
# 123456@127.0.0.1:5432

Base = declarative_base()

Session = sessionmaker()