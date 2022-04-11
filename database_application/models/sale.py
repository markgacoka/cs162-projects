from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import column_property
from sqlalchemy.sql import case
from database import Base

class Sale(Base): 
    """A model for the transactions taken to buy a home.

    Args:
        sale_id (int): A primary key for the Sale table.
        buyer_id (int): A foreign key for the Buyer table.
        agent_id (int): A foreign key for the Agent table.
        house_id (int): A foreign key for the House table.
        sale_price (float): The price the house was sold for.
        selling_date (datetime): The date the house was sold.
        agent_commission (float): The commission received by the listing agent after selling a house.
        

    Returns:
        str: The ID, house ID and selling price of the listing.
    """
    __tablename__ = 'sale'
    sale_id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("buyer.buyer_id"))
    agent_id = Column(Integer, ForeignKey("agent.agent_id"))
    house_id = Column(Integer, ForeignKey("house.house_id"))
    sale_price = Column(Float, unique=False)
    selling_date = Column(Date)
    agent_commission = column_property(sale_price * case(
        [
            (sale_price < 100000, 0.1),
            (sale_price < 200000, 0.075),
            (sale_price < 500000, 0.06),
            (sale_price < 1000000, 0.05),
        ], else_ = 0.04))

    def __repr__(self):
        return "<Sale ID: {} House: {} Selling Price: {}>".format(self.sale_id, self.house_id, self.sale_price)