import face_recognition
import cv2
import os
import time

data_path = "/home/centos/goldeneye/uploads/9db593a8/subprocessing/images"

t1 = time.time()

images = []
img_name = []

for filename in os.listdir(data_path):
    if filename.endswith('.jpg'):
        img_path = os.path.join(data_path, filename)
        images.append(img_path)
        img_name.append(filename)


def compare(image1, image2):
    img = cv2.imread(image1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        img_encoding = face_recognition.face_encodings(rgb_img)[0]
    except Exception as err:
        os.remove(image1)

    img2 = cv2.imread(image2)
    rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    try:
        img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
        result = face_recognition.compare_faces([img_encoding], img_encoding2)
        
        if result == [True]:
            os.remove(image2)
    except Exception as err:
        os.remove(image2)
    
def resetDirect():
    images1 = []
    img_name1 = []
    for filename in os.listdir(data_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(data_path, filename)
            images1.append(img_path)
            img_name1.append(filename)

    images.clear()
    img_name.clear()
    img_name.extend(img_name1)
    for img in images1:
        images.append(img)
        
while True:
    for i, img1 in enumerate(images):

        if len(images) == 1:
            os.replace(img1, fr'/home/centos/goldeneye/uploads/9db593a8/subprocessing/unique_images/{img_name[i]}')
            
        for img2 in images:

            if img1 == img2:
                continue

            try:
                compare(img1, img2)

            except:
                continue 

        try:
            os.replace(img1, fr'/home/centos/goldeneye/uploads/9db593a8/subprocessing/unique_images/{img_name[i]}')

        except:
            continue

        resetDirect()
    
    if len(images)==0:
        break

