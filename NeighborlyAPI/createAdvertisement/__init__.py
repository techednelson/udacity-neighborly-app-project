import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = 'mongodb://micro-cosmos-db:Zy9dFcg3nIm0udQm7NP6z8IaiFNg6164JbA9x4aX20rDEh9nhOoDf7NGSBZhMkJePs5SbDZ3ZHtN1IS2x5GNhQ==@micro-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
            client = pymongo.MongoClient(url)
            database = client['micro-mongo-db']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
