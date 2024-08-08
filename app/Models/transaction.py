# Models/transaction.py
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Enum
from Models.base import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    trans_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_table.user_id'))
    ticker = Column(String(10), nullable=False)
    trans_type = Column(Enum('buy', 'sell'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_charge = Column(DECIMAL(10, 2), nullable=False)
    tot_amnt = Column(DECIMAL(15, 2), nullable=False)
