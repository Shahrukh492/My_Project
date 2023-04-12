import boto3
import mysql.connector
from datetime import datetime
import os
from datetime import datetime
now = datetime.now()
Date_time = now.strftime("%Y/%m/%d %H:%M:%S")
src_path = "/geyeaicameraphotos/"
dst_path = "/geyeaicameraphotos/DONE/"
dst_path1 = "/Manisha/invalidfacesphotos/"

mydb = mysql.connector.connect(
  host="ls-06e0be461c23a056c1d8682155d97b5ec717b111.cfk9loxupdqd.ap-south-1.rds.amazonaws.com",
  user="dbmasteruser",
  password="ConsultIT1!",
  database="dbmaster"
)

print(mydb.get_server_info())
