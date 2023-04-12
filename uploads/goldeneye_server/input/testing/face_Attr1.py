import time
import boto3
from datetime import date

today = date.today()
start = time.time()
def dectFace(photo):
    client = boto3.client('rekognition', 
                        aws_access_key_id='AKIAYTW5WOZ3TLDRQHHS', aws_secret_access_key='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',region_name='ap-south-1')
    with open (photo, 'rb') as source_image:
        source_bytes = source_image.read()
    response = client.detect_faces(Image={'Bytes': source_bytes},
    Attributes = ['ALL'])
    print('Detected faces for ' + photo)
    end = time.time()
    time_elapsed = end - start
    text_file = open("/home/centos/goldeneye/Shahrukh/Logs/Face_Attr/{}.txt".format(str(today)), "a")
    text_file.write(str(photo)+' =======> ' + str(response))
    text_file.write("\n")
    text_file.close()
    return response

