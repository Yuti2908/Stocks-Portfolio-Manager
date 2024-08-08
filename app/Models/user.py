# Models/user.py
from sqlalchemy import Column, Integer, String, DECIMAL
from Models.base import Base

class User(Base):
    __tablename__ = 'user_table'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    pwd = Column(String(255), nullable=False)
    realised_profit = Column(DECIMAL(15, 2), default=0.00)
    unrealised_profit = Column(DECIMAL(15, 2), default=0.00)
