import boto3
import time
from datetime import date
import os

today = date.today()
start = time.time()
#text_file = open("Shahrukh/Logs/SearchFaces/{}.txt".format(str(today)), "a")

def search_face(photo):
    try:
        bucket='geyeaicameraphotos'
        collectionId='geyefacescollection'
        #fileName='1.jpg'
        threshold = 50
        maxFaces=1
        client=boto3.client('rekognition', region_name="ap-south-1")
        response=client.search_faces_by_image(CollectionId=collectionId,
                                    Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                    FaceMatchThreshold=threshold,
                                    MaxFaces=maxFaces)
        faceMatches=response['FaceMatches']
        #print(faceMatches)
        print('Matching faces')
        for match in faceMatches:
            face_id = match['Face']['FaceId']
            print ('FaceId:' + face_id)
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
        end = time.time()
        time_elapsed = end - start
        print("Execution Time of SearchFacesByImageinColl Program: ", time_elapsed)
        text_file1 = open("Shahrukh/Logs/SearchFaces/{}.txt".format(str(today)), "a")
        text_file1.write("Done : Search Face in Collections"+"----"+"Func Name : search_face"+"----"+"ProgramFile Name : SearchFacesByImageinColl1.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file1.write("\n")
        text_file1.close()
        return faceMatches

    except Exception as e:
        print(e)
        end = time.time()
        time_elapsed = end - start
        print("Execution Time of SearchFacesByImageinColl Program: ", time_elapsed)
        text_file1 = open("Shahrukh/Logs/SearchFaces/{}.txt".format(str(today)), "a")
        text_file1.write("Not Done : Getting Errror"+"----"+"Error Name : "+str(e)+"----"+"Func Name : search_face"+"----"+"ProgramFile Name : SearchFacesByImageinColl1.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file1.write("\n")
        text_file1.close()

#src_path = "/geyeaicameraphotos/WIP/"
#list_of_files = os.listdir(src_path)
#for file in list_of_files:
    #search_face(file)   
#search_face('bbf092f7_2022-06-16_15-44-06.jpg')
