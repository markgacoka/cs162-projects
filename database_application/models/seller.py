from sqlalchemy import Column, Integer, String
from database import Base
    
class Seller(Base): 
    """A model for the seller who sells a house.

    Args:
        seller_id (int): Primary key for the Seller table.
        seller_first_name (str): The first name of the seller.
        seller_surname (str): The last name of the seller.
        seller_phone_number (str): The phone number for the seller.
        seller_email (str): The email for the seller.

    Returns:
        str: The full name of the seller.
    """
    __tablename__ = 'seller'
    seller_id = Column(Integer, primary_key=True, index=True)
    seller_first_name = Column(String(250), unique=False, nullable=False)
    seller_surname = Column(String(250), unique=False, nullable=True)
    seller_phone_number = Column(Integer, unique=False, nullable=True)
    seller_email = Column(String(250), unique=False, nullable=True)

    def __repr__(self):
        return "<Seller: {}>".format(self.seller_first_name + self.seller_surname)