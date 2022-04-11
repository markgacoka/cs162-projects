import os, sys
sys.path.insert(0, os.getcwd())

import unittest
from database import Base
from models.house import House
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def wrong_input_column(self):
    try:
        self.example_house_2 = House(
            bedrooms = 2,
            bathrooms = 5,
            kitchens = 10,
            address = '888 City Center, San Francisco, CA',
            zip_code = 92231
        )
        self.session.add(self.example_house_2)
    except TypeError:
        raise Exception('Wrong column or data type added!')

class TestQuery(unittest.TestCase):
    # Set up a mock database to test if queries are added successfully
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)
        self.example_house = House(
            bedrooms = 2,
            bathrooms = 3,
            address = '515 Market Street, San Francisco, CA',
            zip_code = 92231
        )
        self.session.add(self.example_house)
        self.session.commit()
        
    # Test if the house row is added to the model
    def test_house_model(self):
        expected = [self.example_house]
        result = self.session.query(House).all()
        self.session.commit()
        self.assertEqual(result, expected)
        
    # Test if the house row is deleted from the model
    def test_house_model(self):
        expected = []
        self.session.query(House).filter(House.house_id==1).delete()
        result = self.session.query(House).all()
        self.session.commit()
        self.assertEqual(result, expected)
        
    # Test a wrong input parameters by adding false columns
    def test_house_model(self):
        with self.assertRaises(Exception) as context:
            wrong_input_column(self)
        self.assertTrue(context.exception, 'Wrong column or data type added!')

    # Delete the database
    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        
if __name__ == '__main__':
    unittest.main()