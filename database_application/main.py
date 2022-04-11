from datetime import datetime
from database import engine, Base
from create import generate_test_data

if __name__ == '__main__':
    # Initialize the tables and load the synthetic data
    print("{} Creating data...".format(datetime.now()))
    Base.metadata.create_all(engine)
    generate_test_data()
    print("{} COMPLETED!".format(datetime.now()))