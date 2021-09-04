import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

def get_database():
    client = MongoClient(os.getenv('MONGO_DB_CONNECTION_STRING'))
    return client['billbotdb']


if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()