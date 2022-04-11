from datetime import date
from database import session
from models.commission import Commission
from models.sale import Sale
from models.listing import Listing
from models.house import House
from models.buyer import Buyer
from models.seller import Seller
from models.agent import Agent
from models.office import Office
from models.agent_offices import AgentOffices
from models.total_sales import TotalSales

# A list of synthetic records to be added to the database
# [AgentID], AgentName, AgentSurname, AgentPhone, AgentEmail
agents = {
    '1': ['Ryan', 'Serhant', '(415) 234-2345', 'rserhant@realventures.com', 0],
    '2': ['Jason', 'Oppenheim', '(628) 763-5900', 'joppenheim@yahoo.com', 0],
    '3': ['Josh', 'Flagg', '(415) 998-2736', 'joshf@realventures.com', 0],
    '4': ['Jade', 'Mills', '(628) 933-5564', 'jademills@gmail.com', 0],
    '5': ['Josh', 'Altman', '(415) 222-5637', 'joshaltman@realventures.com', 0],
}

# [BuyerID], BuyerName, BuyerSurname, BuyerPhone, BuyerEmail
buyers = {
    '1': ['Gacoka', 'Mbui', '(415) 234-2348', 'gacoka@gmail.com'],
    '2': ['Philip', 'Sterne', '(555) 234-8927', 'psterne@hotmail.com'],
    '3': ['John', 'Goldberg', '(622) 893-6777', 'johngold@gmail.com'],
    '4': ['Amy', 'Schlute', '(919) 223-4763', 'amyamy@yahoo.com'],
    '5': ['Jane', 'Steward', '(772) 837-6545', 'janestew@microsoft.com']
}

# [SellerID], SellerName, SellerSurname, SellerPhone, SellerEmail
sellers = {
    '1': ['Jason T.', 'Whelan', '(515) 275-4823', 'jasonwhelan@gmail.com'],
    '2': ['Herman A.', 'Smith', '(908) 735-6445', 'hermans@gmail.com'],
    '3': ['Ruby', 'Diaz', '(607) 898-3311', 'rdiaz@google.com'],
    '4': ['Martha', 'Ferrari', '(585) 444-0235', 'marthaferr@hotmail.com'],
    '5': ['Susan M.', 'Stone', '(410) 287-2517', 'susanstone@yahoo.com'],
}

# [OfficeID], OfficeName, Address, ZipCode
offices = {
    '1': ['San Francisco HQ', '1125 Market Street, San Francisco', 92022],
    '2': ['New York Office', '4547 Gile Hollow Rd Hinsdale, New York', 14743],
    '3': ['Maryland Office', '2515 Blue Water Blvd Odenton, Maryland', 2113],
    '4': ['Iowa Office', '711 High St Des Moines, Iowa', 50309],
}

# [HouseID], Bedrooms, Bathrooms, Address, ZipCode, OfficeID
houses = {
    '1': [3, 3, '512 Wooden Creek, San Diego, California', 92002, 1],
    '2': [3, 2, '3221 West Hollywood, California', 7382, 1],
    '3': [8, 5, '95 Harrogate Xing West Henrietta, New York', 11273, 2],
    '4': [6, 5, '216 Thomas Ave North East, Maryland', 9865, 3],
    '5': [7, 6, '119 S 1st St Ogden, Iowa', 2253, 4],
    '6': [2, 3, '3799 State Street Rd Bay City, Iowa', 48706, 4],
    '7': [3, 3, '625 Main St Pinetown, San Francisco, California', 27865, 1],
}

# [ListingID], SellerID, AgentID, HouseID, ListingPrice, ListingDate, isSold
listings = {
    '1': [1, 1, 1, 2000000.00, date(2021, 12, 24), True],
    '2': [2, 1, 2, 3000000.00, date(2022, 1, 13), True],
    '3': [3, 2, 3, 14500000.00, date(2022, 2, 2), False],
    '4': [4, 4, 4, 10000000.00, date(2022, 3, 1), True],
    '5': [5, 3, 5, 55000000.00, date(2022, 3, 3), True],
    '6': [2, 5, 6, 5000000.00, date(2022, 3, 13), True],
    '7': [3, 1, 7, 8000000.00, date(2022, 3, 20), True],
}

# [SaleID], BuyerID, AgentID, HouseID, SalePrice, SellingDate
sales = {
    '1': [1, 1, 1, 1500000.00, date(2021, 12, 30)],
    '2': [2, 1, 2, 2800000.00, date(2022, 2, 15)],
    '3': [3, 4, 4, 15500000.00, date(2022, 3, 25)],
    '4': [3, 3, 5, 66800000.00, date(2022, 3, 27)],
    '5': [4, 5, 6, 6200000.00, date(2022, 3, 28)],
    '6': [2, 1, 7, 10000000.00, date(2022, 3, 30)]
}

# [AgentOfficesID], AgentID, OfficeID
agent_offices = {
    '1': [1, 1],
    '2': [2, 1],
    '3': [3, 2],
    '4': [4, 4],
    '5': [5, 3]
}

# Add each row and save it to the database
def generate_test_data(): 
    for idx, agent_details in agents.items():
        example_agent = Agent(
            agent_id = int(idx),
            agent_first_name = agent_details[0],
            agent_surname = agent_details[1],
            agent_phone_number = agent_details[2],
            agent_email = agent_details[3],
        )
        session.add(example_agent)
        
    for idx, buyer_details in buyers.items():
        example_buyer = Buyer(
            buyer_id = int(idx),
            buyer_first_name = buyer_details[0],
            buyer_surname = buyer_details[1],
            buyer_phone_number = buyer_details[2],
            buyer_email = buyer_details[3],
        )
        session.add(example_buyer)
        
    for idx, house_details in houses.items():
        example_house = House(
            house_id = int(idx),
            bedrooms = house_details[0],
            bathrooms = house_details[1],
            address = house_details[2],
            zip_code = house_details[3],
            office_id = house_details[4]
        )
        session.add(example_house)
        
    for idx, listing_detail in listings.items():
        example_listing = Listing(
            listing_id = int(idx),
            seller_id = listing_detail[0],
            agent_id = listing_detail[1],
            house_id = listing_detail[2],
            listing_price = listing_detail[3],
            listing_date = listing_detail[4],
            is_sold = listing_detail[5]
        )
        session.add(example_listing)
        
    for idx, sale_detail in sales.items():
        example_sale = Sale(
            sale_id = int(idx),
            buyer_id = sale_detail[0],
            agent_id = sale_detail[1],
            house_id = sale_detail[2],
            sale_price = sale_detail[3],
            selling_date = sale_detail[4],
        )
        session.add(example_sale)
    
    for idx, office_detail in offices.items():
        example_office = Office(
            office_id = int(idx),
            office_name = office_detail[0],
            office_address = office_detail[1],
            office_postal_code = office_detail[2],
        )
        session.add(example_office)
    
    for idx, seller_detail in sellers.items():
        example_seller = Seller(
            seller_id = int(idx),
            seller_first_name = seller_detail[0],
            seller_surname = seller_detail[1],
            seller_phone_number = seller_detail[2],
            seller_email = seller_detail[3]
        )
        session.add(example_seller)

    for idx, agent_offices_detail in agent_offices.items():
        example_agent_office = AgentOffices(
            agent_offices_id = int(idx),
            agent_id = agent_offices_detail[0],
            office_id = agent_offices_detail[1]
        )
        session.add(example_agent_office)
    session.add(Commission())
    session.add(TotalSales())
    session.commit()
    session.close()