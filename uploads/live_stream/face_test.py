from imutils import face_utils
import dlib
import cv2
from datetime import datetime
import time
import os
from datetime import date
import concurrent.futures

t1=time.time()

today = date.today()
data_path = 'images/'
detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0)  #connect to mobile camera
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
                    if h > 70 and w > 70:
                        cv2.imwrite(os.path.join(
                                    data_path, f"{now.strftime('%Y-%m-%d %H_%M_%S_%f')}.jpg"), crop_img)
                    else:
                        continue
            except:
                continue
        cv2.imshow("DlibFacee", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

print("*********Face Detection Completed*********")

print("Time taken: ", ((time.time())-t1))

