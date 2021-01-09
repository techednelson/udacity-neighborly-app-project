import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = 'mongodb://micro-cosmos-db:Zy9dFcg3nIm0udQm7NP6z8IaiFNg6164JbA9x4aX20rDEh9nhOoDf7NGSBZhMkJePs5SbDZ3ZHtN1IS2x5GNhQ==@micro-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
        client = pymongo.MongoClient(url)
        database = client['micro-mongo-db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
