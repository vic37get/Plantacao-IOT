from pymongo import MongoClient


def connectMongo(db_name): 
    client = MongoClient('mongodb+srv://vic35get:005EFsVTBrldkZpp@plantacaoiot.fc1r2gv.mongodb.net/?retryWrites=true&w=majority')
    db = client[db_name]
    return db
