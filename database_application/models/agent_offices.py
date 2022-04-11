from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class AgentOffices(Base): 
    """A model for the composite table that links the agents and offices.

    Args:
        agent_offices_id (int): Primary key for the AgentOffices table.
        agent_id (int): A foreign key for the Agent table.
        office_id (int): A foreign key for the Offices table.

    Returns:
        int: The specific ID in the AgentOffices table.
    """
    __tablename__ = 'agentoffice'
    agent_offices_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    agent_id = Column(Integer, ForeignKey("agent.agent_id"))
    office_id = Column(Integer, ForeignKey("office.office_id"))

    def __repr__(self):
        return "<AgentOffice ID: {}".format(self.agent_offices_id)