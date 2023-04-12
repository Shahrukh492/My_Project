import cv2
import dlib
import os
import shutil
from tqdm import tqdm

img_dir_path='/images'
detect_img_dir='detect_img'
not_detect_img_dir='not_detect_dir'

detector=dlib.get_frontal_face_detector()

img_files=[f for f in os.listdir(img_dir_path) if f.endswids('.jpg')]

for img_file in tqdm(img_files):
    img_path=os.path.join(img_dir_path,img_file)
    print(img_path)