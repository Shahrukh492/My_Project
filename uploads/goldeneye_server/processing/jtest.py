import json
import pymongo
try:
    conn=pymongo.MongoClient("mongodb://localhost:27017/")
    db=conn['goldeneye']
    coll=db['myCollection']
    str_form='[{"Datetime":"28/02/2023","FaceID":"63fddbf97e709c665a31e5a3","CameraID":"3c09","H_age":25,"L_age":35,"Gender":"Male"},{"Datetime":"28/02/2023","FaceID":"63fddbf97e709c665a31e5a3","CameraID":"3c09","H_age":25,"L_age":35,"Gender":"Male"},{"Datetime":"28/02/2023","FaceID":"63fddbf97e709c665a31e5a3","CameraID":"3c09","H_age":25,"L_age":35,"Gender":"Male"},{"Datetime":"28/02/2023","FaceID":"63fddbf97e709c665a31e5a3","CameraID":"3c09","H_age":25,"L_age":35,"Gender":"Male"},{"Datetime":"28/02/2023","FaceID":"63fddbf97e709c665a31e5a3","CameraID":"3c09","H_age":25,"L_age":35,"Gender":"Male"}]'
    data=json.loads(str_form)
    
    for doc in data:
        coll.insert_one(doc)
    print("Done")
    cur=coll.find()
    for docs in cur:
        print(docs)
except Exception as err:
    print("Not Connected to MongoDB")