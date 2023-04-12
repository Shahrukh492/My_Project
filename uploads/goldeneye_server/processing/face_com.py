import face_recognition
import cv2
import os

data_path = "/A_goldeneye/uploads/goldeneye_server/processing/images"

# Load all images and their corresponding filenames
images = []
img_names = []
for filename in os.listdir(data_path):
    if filename.endswith('.jpg'):
        img_path = os.path.join(data_path, filename)
        images.append(cv2.imread(img_path))
        img_names.append(filename)

# Find duplicates by comparing each image to all others
duplicates = set()
for i in range(len(images)):
    for j in range(i+1, len(images)):
        if face_recognition.compare_faces([face_recognition.face_encodings(images[i])[0]],face_recognition.face_encodings(images[j])[0])[0]:
            duplicates.add(i)
            duplicates.add(j)

# Remove duplicates
for i in duplicates:
    os.remove(os.path.join(data_path, img_names[i]))
print("Done")