import os, sys
sys.path.insert(0, os.getcwd())

from database import session
from sqlalchemy import insert

from models.sale import Sale
from models.buyer import Buyer
from models.agent import Agent
from models.house import House
from models.office import Office
from models.listing import Listing
from models.agent_offices import AgentOffices
from models.total_sales import TotalSales

# The actual data is added in create.py
# Adds a transaction
def transaction(sale):
    try: 
        session.execute(insert(Sale), [sale])
        session.query(Listing).filter(Listing.house_id == sale['house_id']).update(
            {Listing.is_sold: True}, synchronize_session=False
        )
        session.query(TotalSales).filter(TotalSales.total_sales_id == 1).update(
            {TotalSales.total_sales: TotalSales.total_sales + sale['selling_price']},
            synchronize_session=False
        )
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

session.commit()
        
# Displays all the tables' data
print(session.query(Buyer).all())
print(session.query(Agent).all())
print(session.query(Office).all())
print(session.query(AgentOffices).all())
print(session.query(House).all())
print(session.query(Listing).all())
print(session.query(Sale).all())
print(session.query(TotalSales).all())