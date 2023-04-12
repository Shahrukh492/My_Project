import boto3
import json
import time
from datetime import date
import os

today = date.today()
start = time.time()

def detect_faces(photo):
    
    try:
        bucket = 'geyeaicameraphotos'
        client=boto3.client('rekognition', aws_access_key_id='AKIAYTW5WOZ3TLDRQHHS', aws_secret_access_key='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',region_name='ap-south-1')
        response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
        print(response)
        print('Detected faces for ' + photo)
        for faceDetail in response['FaceDetails']:
            print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
            print('Here are the other attributes:')
            print(json.dumps(faceDetail, indent=4, sort_keys=True))
            # Access predictions for individual face details and print them
            print("Gender: " + str(faceDetail['Gender']))
            print("Smile: " + str(faceDetail['Smile']))
            print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
            print("Emotions: " + str(faceDetail['Emotions'][0]))
            print("Faces detected: " + str(len(response['FaceDetails'])))
        end = time.time()
        time_took = end - start
        print("Execution Time of ReadFaceAttr Program: ", time_took)
        text_file = open("Shahrukh/Logs/ReadFaceAttr/{}.txt".format(str(today)), "a")
        text_file.write("Done : Getting Face Attributes"+"----"+"Func Name : detect_faces"+ "----"+"ProgramFile Name : ReadFaceAttr1.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file.write("\n")
        text_file.close()
        return response

    except Exception as e:
        print(e)
        end = time.time()
        time_took = end - start
        print("Execution Time of ReadFaceAttr Program: ", time_took)
        text_file = open("Shahrukh/Logs/ReadFaceAttr/{}.txt".format(str(today)), "a")
        text_file.write("Not Done : Getting Errror"+"----"+"Error Name : "+str(e)+"----"+"Func Name : detect_faces"+"----"+"ProgramFile Name : ReadFaceAttr1.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file.write("\n")
        text_file.close()

#detect_faces('bbf092f7_2022-06-22_13-28-42.jpg')

