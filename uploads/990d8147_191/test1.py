import boto3
from ReadFaceAttr import *
from SearchFacesByImageinColl import *
from Add_img_col import * 
import mysql.connector
from datetime import datetime,time
import os
from datetime import date
import shutil

start = time.time()
now = datetime.now()
Date_time = now.strftime("%Y_%M_%D_%I:%M:%S")
src_path = "processed/"
dst_path = "processed/"
dst_path1 = "Shahrukh/invalidfacesphotos/"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Sheikh@7065",
  database="srkdb"
)

bucket='geyeaicameraphotos'

def Images():
    list_of_files = filter( lambda x: os.path.isfile(os.path.join(src_path, x)),
                        os.listdir(src_path) )
    return list_of_files

def insert(photo, deviceid):
    json_data = detect_faces(photo)
    json_value = str(json_data)
    json_value1 = json.dumps(json_value)
    face = search_face(photo)
    
    
    try:
        if len(face) == 0:
            faceIdNew = add_faces_to_collection(photo)
            mycursor = mydb.cursor()
            sql = "INSERT INTO GEYE_CAMERAFACESLOG (FACESTRINGAWS, DATETIMECREATED, CAMERAID, FACEIDAWS, PHOTOFILENAME) \
            VALUES (%s, %s, %s, %s, %s)"
            val = (json_value1, Date_time, deviceid, faceIdNew, photo)
            mycursor.execute(sql, val)
            mydb.commit()
            new_src = os.path.join(src_path, photo)
            new_dst = os.path.join(dst_path, photo)
            print(mycursor.rowcount, "record inserted.")
            #shutil.move(new_src, new_dst)
            print("File moves to Done Folder")
            end = time.time()
            time_elapsed = end - start
            print("Program exec time: ", time_elapsed)
            text_file = open("Shahrukh/Logs/WriteMysql/{}.txt".format(str(today)), "a")
            text_file.write("Done : Data Inserted for New face Image with New FaceID"+"----"+"Func Name : insert"+ "----"+"ProgramFile Name : WriteMysql.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
            text_file.write("\n")
            text_file.close()

        elif len(face) != 0:
                for match in face:
                    faceIdOld = match['Face']['FaceId']
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO GEYE_CAMERAFACESLOG (FACESTRINGAWS, DATETIMECREATED, CAMERAID, FACEIDAWS, PHOTOFILENAME) \
                    VALUES (%s, %s, %s, %s, %s)"
                    val = (json_value1, Date_time, deviceid, faceIdOld, photo)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    new_src = os.path.join(src_path, photo)
                    new_dst = os.path.join(dst_path, photo)
                    print(mycursor.rowcount, "record inserted.")
                    #shutil.move(new_src, new_dst)
                    print("File moves to Done Folder")
                    end = time.time()
                    time_elapsed = end - start
                    print("Execution Time of WriteMysql Program: ", time_elapsed)
                    text_file = open("Shahrukh/Logs/WriteMysql/{}.txt".format(str(today)), "a")
                    text_file.write("Done : Data Inserted for Existing face with Existing FaceID"+"----"+"Func Name : insert"+ "----"+"ProgramFile Name : WriteMysql.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
                    text_file.write("\n")
                    text_file.close()
        

    except Exception as e:
        print(e)
        mycursor = mydb.cursor()
        sql = "INSERT INTO INVALIDFACEPHOTOS_LOG (DATETIMECREATED, DEVICEID, PHOTOFILENAME) \
        VALUES (%s, %s, %s)"
        val = (Date_time, deviceid, photo)
        mycursor.execute(sql, val)
        mydb.commit()
        end = time.time()
        time_elapsed = end - start
        print("Program execution time: ", time_elapsed)
        new_src = os.path.join(src_path, photo)
        new_dst1 = os.path.join(dst_path1, photo)
        #shutil.move(new_src, new_dst1)
        text_file = open("Shahrukh/Logs/WriteMysql/{}.txt".format(str(today)), "a")
        text_file.write("Not Done : Getting Errror"+"----"+"Error Name : "+str(e)+"----"+"Func Name : insert"+"----"+"ProgramFile Name : WriteMysql.py"+"----"+"Program execution time : "+str(time_elapsed)+"----"+"For image : "+str(photo))
        text_file.write("\n")
        text_file.close()

Name_Of_File = Images()
for file in Name_Of_File:
    print(file)
    split_value = file.split("_")
    device_id = split_value[0]
    #print(device_id)
    insert(file, device_id)
