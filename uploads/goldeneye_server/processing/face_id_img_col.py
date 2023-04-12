import boto3
from datetime import date
import os
from datetime import datetime

today = date.today()
ttime = datetime.now()
now = ttime.strftime('%m-%d %H')
now = datetime.now()
Date_time = now.strftime("%Y_%m_%d__%H_%M_%S")

def add_faces_to_collection(target_file, photo):
    client = boto3.client('rekognition', 
                        aws_access_key_id='AKIAYTW5WOZ3TLDRQHHS', aws_secret_access_key='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',region_name='ap-south-1')

    imageTarget = open(target_file, 'rb')

    response = client.index_faces(CollectionId='geyefacescollection',
                                  Image={'Bytes': imageTarget.read()},
                                  ExternalImageId=photo,
                                  MaxFaces=1,
                                  QualityFilter="AUTO",
                                  DetectionAttributes=['ALL'])
    print(response)

    print('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print('  Face ID: ' + faceRecord['Face']['FaceId'])
        print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
        print('  Image ID: {}'.format(faceRecord['Face']['ImageId']))
        print('  External Image ID: {}'.format(faceRecord['Face']['ExternalImageId']))
        print('  Confidence: {}'.format(faceRecord['Face']['Confidence']))

        face_id = faceRecord['Face']['FaceId']
        text_file = open("E:/My_Project/uploads/goldeneye_server/Shahrukh/Logs/Add_img_col/{}.txt".format(str(today)), "a")

        text_file.write(str(target_file)+' =======> ' + str(face_id))
        text_file.write("\n")
        text_file.close()
        

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    text_file1 = open("jsonfile/{}.txt".format(str(today)), "a")
    text_file1.write(str(target_file)+'=======>'+str(response))
    text_file1.write("\n")
    text_file1.close()
    # return face_id


if __name__ == '__main__':
    data_path = 'E:/My_Project/uploads/goldeneye_server/processing/images'
    images = []
    images1 = []
    for filename in os.listdir(data_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(data_path, filename)
            images.append(img_path)
            images1.append(filename)
    
    for i,file in enumerate(images):
        print(file)
        img = f"{Date_time}.jpg"
        device_id = '9db593a8'
        add_faces_to_collection(file, img)