from sqlalchemy import Column, Integer, ForeignKey, Float, Date, Boolean, func
from database import Base

class Listing(Base): 
    """A model for the listing of a home.

    Args:
        listing_id (int): A primary key for the Listing table.
        seller_id (int): A foreign key for the Seller table.
        agent_id (int): A foreign key for the Agent table.
        house_id (int): A foreign key for the House table.
        listing_price (float): The price the house was listed for.
        listing_date (datetime): The date the house was listed on the market.
        is_sold (bool): A boolean value of whether the house was sold or not.

    Returns:
        str: The ID, house ID and listing price of the listing.
    """
    __tablename__ = 'listing'
    listing_id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("seller.seller_id"))
    agent_id = Column(Integer, ForeignKey("agent.agent_id"))
    house_id = Column(Integer, ForeignKey("house.house_id"))
    listing_price = Column(Float, unique=False)
    listing_date = Column(Date, default=func.now())
    is_sold = Column(Boolean)

    def __repr__(self):
        return "<Listing ID: {} House: {} Listing Price: {}>".format(self.listing_id, self.house_id, self.listing_price)