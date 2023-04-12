import boto3
from datetime import date

today = date.today()

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
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        face_id = faceRecord['Face']['FaceId']
        text_file = open("/home/centos/goldeneye/Shahrukh/Logs/Add_img_col/{}.txt".format(str(today)), "a")

        text_file.write(str(target_file)+' =======> ' + str(response))
        text_file.write("\n")
        text_file.close()

