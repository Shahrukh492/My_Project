from imutils import face_utils
import dlib
import cv2
from datetime import datetime
import os
from datetime import date
import concurrent.futures

today = date.today()
data_path = '/home/centos/goldeneye/uploads/3c01cc89/processing/images'
detector = dlib.get_frontal_face_detector()

video_path = '/home/centos/goldeneye/uploads/3c01cc89/processing/video'
videos = []
for filename in os.listdir(video_path):
    if filename.endswith('.mp4'):
        vid_path = os.path.join(video_path,filename)
        videos.append(vid_path)

def faceDect(vid):
    cap = cv2.VideoCapture(vid)
    while cap.isOpened():

        success, image = cap.read()

        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        except Exception as err:
            break

        else:

            rects = detector(gray, 1)

            for (i, rect) in enumerate(rects):

                (x, y, w, h) = face_utils.rect_to_bb(rect)
                square = cv2.rectangle(image, (x, y), ((x + 25) + (w + 25), (y + 25) + h + 25), (0, 255, 0), 2)
                crop_img = image[y:(y + 25) + (h + 25), x:(x + 25) + (w + 25)]
                
                now = datetime.now()
                try:
                    if rect:
                        if h > 65 and w > 65:
                            cv2.imwrite(os.path.join(
                                        data_path, f"{now.strftime('%Y-%m-%d %H_%M_%S_%f')}.jpg"), crop_img)
                        else:
                            continue
                except:
                    continue
            
            
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor()as executor:
        executor.map(faceDect, videos)
    for vids in videos:
        os.remove(vids)

    print("Face Detection Completed")
