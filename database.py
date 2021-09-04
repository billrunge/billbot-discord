from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

def database():
    dbclient = MongoClient(os.getenv('MONGO_DB_CONNECTION_STRING'))
    db = dbclient.test