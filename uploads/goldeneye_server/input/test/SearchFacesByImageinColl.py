import boto3
import time
from datetime import date

today = date.today()
start = time.time()

def search_face(photo):
    try:
        collectionId='geyefacescollection'
        threshold = 50
        maxFaces=1
        with open (photo, 'rb') as source_image:
            source_bytes = source_image.read()
        client=boto3.client('rekognition', aws_access_key_id='AKIAYTW5WOZ3TLDRQHHS',
         aws_secret_access_key='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',region_name='ap-south-1')
        response=client.search_faces_by_image(CollectionId=collectionId,
                                    Image={'Bytes': source_bytes},
                                    FaceMatchThreshold=threshold,
                                    MaxFaces=maxFaces)
        faceMatches=response['FaceMatches']
        print('Matching faces')
        for match in faceMatches:
            face_id = match['Face']['FaceId']
        end = time.time()
        time_elapsed = end - start
        text_file1 = open("/home/centos/goldeneye/Arsalan/logs/SearchFaces/{}.txt".format(str(today)), "a")
        text_file1.write("Done : Search Face in Collections"+"----"+"Func Name : search_face"+"----"+"ProgramFile Name : SearchFacesByImageinColl1.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file1.write("\n")
        text_file1.close()
        return faceMatches

    except Exception as e:
        print(e)
        end = time.time()
        time_elapsed = end - start
        text_file1 = open("/home/centos/goldeneye/Arsalan/logs/SearchFaces/{}.txt".format(str(today)), "a")
        text_file1.write("Not Done : Getting Errror"+"----"+"Error Name : "+str(e)+"----"+"Func Name : search_face"+"----"+"ProgramFile Name : SearchFacesByImageinColl1.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file1.write("\n")
        text_file1.close()

