from sqlalchemy import Column, Integer, String
from database import Base
    
class Buyer(Base): 
    """A model for the buyer who purchases a house.

    Args:
        buyer_id (int): Primary key for the Buyer table.
        buyer_first_name (str): The first name of the buyer.
        buyer_surname (str): The last name of the buyer.
        buyer_phone_number (str): The phone number for the buyer.
        buyer_email (str): The email for the buyer.

    Returns:
        str: The full name of the buyer.
    """
    __tablename__ = 'buyer'
    buyer_id = Column(Integer, primary_key=True, index=True)
    buyer_first_name = Column(String(250), unique=False, nullable=False)
    buyer_surname = Column(String(250), unique=False, nullable=True)
    buyer_phone_number = Column(String(20), unique=False, nullable=True)
    buyer_email = Column(String(250), unique=False, nullable=True)
    
    def __repr__(self):
        return "<Buyer: {}>".format(self.buyer_first_name + self.buyer_surname)