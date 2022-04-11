from sqlalchemy import Column, Integer, ForeignKey, Numeric
from database import Base

class Commission(Base):
    """A table for the commissions for a particular agent.

    Args:
        commission_id (int): Primary key for the Commission table.
        agent_id (int): The foreign key in the Agent table.
        monthly_commission (float): The amount of commission an agent received in a month.

    Returns:
        str: The ID and amount of commission received by an agent.
    """
    __tablename__ = 'commission'
    commission_id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(Integer, ForeignKey("agent.agent_id"))
    monthly_commission = Column(Numeric)

    def __repr__(self):
        return "<Commission ID={}, Monthly_commission={}>".format(self.commission_id, self.monthly_commission)