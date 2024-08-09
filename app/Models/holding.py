# Models/holding.py
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from Models.base import Base

class Holding(Base):
    __tablename__ = 'holdings'

    holdings_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_table.user_id'))
    ticker = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)
    avg_purchasing_price = Column(DECIMAL(10, 2), nullable=False)
    current_value = Column(DECIMAL(10, 2), nullable=False)
