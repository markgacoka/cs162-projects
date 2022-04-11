from sqlalchemy import Column, Integer, String
from database import Base

class Agent(Base):
    """A model for the listing agent who connects the buyer and the seller.

    Args:
        agent_id (int): Primary key for the Agent table.
        agent_first_name (str): The first name of the listing agent.
        agent_surname (str): The last name of the listing agent.
        agent_phone_number (str): The phone number for the listing agent.
        agent_email (str): The email for the listing agent.

    Returns:
        str: The full name of the agent.
    """
    __tablename__ = 'agent'
    agent_id = Column(Integer, primary_key=True)
    agent_first_name = Column(String(250), unique=False)
    agent_surname = Column(String(250), unique=False)
    agent_phone_number = Column(String(20), unique=False)
    agent_email = Column(String(250), unique=False)
    
    def __repr__(self):
        return "<Agent: {}>".format(self.agent_first_name + self.agent_surname)