# Models/watchlist.py
from sqlalchemy import Column, Integer, String, ForeignKey
from Models.base import Base

class Watchlist(Base):
    __tablename__ = 'watchlist'

    watchlist_id = Column(Integer, primary_key=True, autoincrement=True)
    watchlist_name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user_table.user_id'))
    ticker = Column(String(10), nullable=False)
