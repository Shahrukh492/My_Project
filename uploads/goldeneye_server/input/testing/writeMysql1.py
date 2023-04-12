from face_Attr import *
from SearchFacesByImageinColl import *
from Add_img_col import * 
import mysql.connector
from datetime import datetime
import os
import json

start = time.time()
now = datetime.now()
Date_time = now.strftime("%Y_%m_%d__%H_%M_%S")

mydb = mysql.connector.connect(
  host="ls-06e0be461c23a056c1d8682155d97b5ec717b111.cfk9loxupdqd.ap-south-1.rds.amazonaws.com",
  user="dbmasteruser",
  password="ConsultIT1!",
  database="dbmaster"
)


data_path = '/home/centos/goldeneye/uploads/9db593a8/processing/unique_images'
images = []
images1 = []
for filename in os.listdir(data_path):
    if filename.endswith('.jpg'):
        img_path = os.path.join(data_path, filename)
        images.append(img_path)
        images1.append(filename)

def insert(photo, deviceid, target_file, image_name):
    json_data = dectFace(photo)
    json_value = str(json_data)
    json_value1 = json.dumps(json_value)
    Date_time = now.strftime("%Y/%m/%d %H:%M:%S")
    face = search_face(photo)
    
    
    try:
        if len(face) == 0:
            faceIdNew = add_faces_to_collection(photo, target_file)
            mycursor = mydb.cursor()
            sql = "INSERT INTO GEYE_CAMERAFACESLOG (FACESTRINGAWS, DATETIMECREATED, CAMERAID, FACEIDAWS, PHOTOFILENAME) \
            VALUES (%s, %s, %s, %s, %s)"
            val = (json_value1, Date_time, deviceid, faceIdNew, image_name)
            mycursor.execute(sql, val)
            mydb.commit()
            
            print(mycursor.rowcount, "record inserted.")
            text_file = open("/home/centos/goldeneye/Shahrukh/Logs/WriteMysql/{}.txt".format(str(today)), "a")
            text_file.write("Done : Data Inserted for New face Image with New FaceID"+"----"+"Func Name : insert"+ "----"+"ProgramFile Name : WriteMysql.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(image_name))
            text_file.write("\n")
            text_file.close()

        elif len(face) != 0:
                for match in face:
                    faceIdOld = match['Face']['FaceId']
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO GEYE_CAMERAFACESLOG (FACESTRINGAWS, DATETIMECREATED, CAMERAID, FACEIDAWS, PHOTOFILENAME) \
                    VALUES (%s, %s, %s, %s, %s)"
                    val = (json_value1, Date_time, deviceid, faceIdOld, image_name)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")

                    print("File moves to Done Folder")
                    end = time.time()
                    time_elapsed = end - start
                    print("Execution Time of WriteMysql Program: ", time_elapsed)
                    text_file = open("/home/centos/goldeneye/Shahrukh/Logs/WriteMysql/{}.txt".format(str(today)), "a")
                    text_file.write("Done : Data Inserted for Existing face with Existing FaceID"+"----"+"Func Name : insert"+ "----"+"ProgramFile Name : WriteMysql.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(image_name))
                    text_file.write("\n")
                    text_file.close()
        

    except Exception as e:
        print(e)
        mycursor = mydb.cursor()
        sql = "INSERT INTO INVALIDFACEPHOTOS_LOG (DATETIMECREATED, DEVICEID, PHOTOFILENAME) \
        VALUES (%s, %s, %s)"
        val = (Date_time, deviceid, image_name)
        mycursor.execute(sql, val)
        mydb.commit()
        end = time.time()
        time_elapsed = end - start
        text_file = open("/home/centos/goldeneye/Shahrukh/Logs/WriteMysql/{}.txt".format(str(today)), "a")
        text_file.write("Not Done : Getting Errror"+"----"+"Error Name : "+str(e)+"----"+"Func Name : insert"+"----"+"ProgramFile Name : WriteMysql.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(image_name))
        text_file.write("\n")
        text_file.close()


for i,file in enumerate(images):
    print(file)
    img = f"{Date_time}.jpg"
    device_id = '9db593a8'
    img_name = images1[i]
    insert(file, device_id, img, img_name)
    os.replace(file, f'/home/centos/goldeneye/uploads/9db593a8/processed/done/{img_name}')

