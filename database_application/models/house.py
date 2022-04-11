from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
    
class House(Base): 
    """A model for the details about the house to be bought.

    Args:
        house_id (int): A primary key for the House table.
        bedrooms (int): The number of bedrooms in the house.
        bathrooms (int): The number of bathrooms in the house.
        address (str): The full address of the listed house.
        zip_code (int): The zip code the house is located in.
        office_id (int): A foreign key of the Office table.

    Returns:
        str: The ID, house ID and selling price of the listing.
    """
    __tablename__ = 'house'
    house_id = Column(Integer, primary_key=True, index=True)
    bedrooms = Column(Integer, unique=False)
    bathrooms = Column(Integer, unique=False)
    address = Column(String(250))
    zip_code = Column(Integer, unique=False)
    office_id = Column(Integer, ForeignKey("office.office_id"))
    
    def __repr__(self):
        return "<House: {}>".format(self.house_id)