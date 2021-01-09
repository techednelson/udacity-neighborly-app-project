import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = 'mongodb://micro-cosmos-db:Zy9dFcg3nIm0udQm7NP6z8IaiFNg6164JbA9x4aX20rDEh9nhOoDf7NGSBZhMkJePs5SbDZ3ZHtN1IS2x5GNhQ==@micro-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
            client = pymongo.MongoClient(url)
            database = client['micro-mongo-db']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
