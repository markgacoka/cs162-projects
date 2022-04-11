from sqlalchemy import Column, Integer, Numeric
from database import Base

class TotalSales(Base): 
    """A model for the all the total sale transactions in a month.

    Args:
        total_sales_id (int): A primary key for the TotalSales table.
        total_sales (float): The total sales as a floating point number.

    Returns:
        float: The total sales.
    """
    __tablename__ = 'totalsales'
    total_sales_id = Column(Integer, primary_key=True, index=True)
    total_sales = Column(Numeric)

    def __repr__(self):
        return "<Total Sales ID: {} Total Sales: {}>".format(self.total_sales_id, self.total_sales)