from sqlalchemy import Column, Integer, String
from database import Base

class Office(Base):
    """A model for the branch offices in Real Ventures.

    Args:
        office_id (int): A primary key for the Office table.
        office_name (str): A name of the office branch in Real Ventures.
        office_address (str): The full address of the office branch.
        office_postal_code (int): The postal code of the office branch.

    Returns:
        str: The name of the office.
    """
    __tablename__ = 'office'
    office_id = Column(Integer, primary_key=True, index=True)
    office_name = Column(String(250), unique=False, nullable=False)
    office_address = Column(String(250), unique=False, nullable=True)
    office_postal_code = Column(Integer, unique=False, nullable=True)

    def __repr__(self):
        return "<Office: {}>".format(self.office_name)