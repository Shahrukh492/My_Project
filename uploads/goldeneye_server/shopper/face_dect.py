import cv2
import dlib
import os
import shutil
from tqdm import tqdm

img_dir_path = "shopper/img"
face_dect_img_path = "shopper/detect"
No_face_dect_img_path = "shopper/not_detect"
detector = dlib.get_frontal_face_detector()

img_files = [f for f in os.listdir(img_dir_path) if f.endswith('.jpg')]

for img_file in tqdm(img_files):
    img_path = os.path.join(img_dir_path, img_file)
    detects(img_path)

def detects(img_path):  
    image = cv2.imread(img_path)
    
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print("Face not found", e)
        shutil.move(img_path, os.path.join(No_face_dect_img_path, img_file))
        print(f"Detection: {img_file} - Sorry this is text not a image, image moved to {No_face_dect_img_path}")
        return
        
    faces = detector(gray)
    
    if len(faces) > 0:
        shutil.move(img_path, os.path.join(face_dect_img_path, img_file))
        print(f"Detection: {img_file} - Face(s) detected, image moved to {face_dect_img_path}")
    else:
        shutil.move(img_path, os.path.join(No_face_dect_img_path, img_file))
        print(f"Detection: {img_file} - No face detected, image moved to {No_face_dect_img_path}")

print("Done")
