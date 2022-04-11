import os, sys
sys.path.insert(0, os.getcwd())
import warnings
from sqlalchemy.exc import SAWarning
warnings.filterwarnings('ignore',
 r"^Dialect sqlite\+pysqlite does \*not\* support Decimal objects natively\, "
 "and SQLAlchemy must convert from floating point - rounding errors and other "
 "issues may occur\. Please consider storing Decimal numbers as strings or "
 "integers on this platform for lossless storage\.$")

from database import session
from models.sale import Sale
from models.agent import Agent
from models.house import House
from models.office import Office
from models.listing import Listing
from models.commission import Commission
from sqlalchemy.schema import Index
from sqlalchemy import func, extract, insert

# Month of March 2022 (01 - 31)
year = 2022
month = 3

# 1. Find the top 5 offices with the most sales for that month.
# Composite tables
# Connect a house's location to a unique place through the office branch its located in.
Index("idx1", House.office_id, House.house_id)
Index("idx2", Sale.selling_date, Sale.sale_price)

# Query
print('Top Offices:')
top_offices = session.query(Office.office_name, Office.office_address, func.sum(Sale.sale_price)) \
    .filter(extract('year', Sale.selling_date) == year, extract('month', Sale.selling_date) == month) \
    .join(House, House.house_id == Sale.house_id) \
    .join(Office, Office.office_id == House.office_id) \
    .group_by(Office.office_id) \
    .order_by(func.sum(Sale.sale_price).desc()) \
    .limit(5) \
    .all()

for office in top_offices:
    print(office)
print('\n')

# 2. Top 5 estate agents who have sold the most
# Composite tables
Index('idx3', Sale.agent_id)

# Query
print('Top Agents:')
top_agents = session.query(Agent.agent_first_name, Agent.agent_surname, Agent.agent_email, Agent.agent_phone_number, func.sum(Sale.sale_price)) \
    .filter(extract('year', Sale.selling_date) == year, extract('month', Sale.selling_date) == month) \
    .join(Agent, Agent.agent_id == Sale.agent_id) \
    .group_by(Sale.agent_id).order_by(func.sum(Sale.sale_price).desc()) \
    .limit(5).all()
for agent in top_agents:
    print(agent)
print('\n')

# 3. Calculate the commission that each estate agent must receive
# Composite tables
Index("idx4", Sale.agent_commission)

# Query
print('Agent Commissions: ')
selection = session.query(Sale.agent_id, func.sum(Sale.agent_commission)) \
    .filter(extract('year', Sale.selling_date) == year, extract('month', Sale.selling_date) == month).group_by(Sale.agent_id)

insert_row = insert(Commission).from_select(names=['agent_id', 'monthly_commission'], select=selection)
session.execute(insert_row)

agent_commission = session.query(Commission).all()
for commission in agent_commission:
    print(commission)
print('\n')

# 4. Average number of days that a sold house was on the market in the month.
# Query
print('Average days of listings on the market:')
avg_days_on_market = session.query(func.avg(func.julianday(Sale.selling_date) - func.julianday(Listing.listing_date))).filter(
    extract('year', Sale.selling_date) == year, extract('month', Sale.selling_date) == month).join(
    Listing, Listing.house_id == Listing.house_id).first()
for day in avg_days_on_market:
    print(day)
print('\n')

# 5. Average selling price for all houses that were sold that month
print('Average selling price for all the houses in the month:')
avg_selling_price = session.query(func.avg(Sale.sale_price)) \
    .filter(extract('year', Sale.selling_date) == year, extract('month', Sale.selling_date) == month).first()
for price in avg_selling_price:
    print(price)
