import mysql.connector as mysql
import pandas as pd

try:
    mySQLCon = mysql.connect(host="ls-06e0be461c23a056c1d8682155d97b5ec717b111.cfk9loxupdqd.ap-south-1.rds.amazonaws.com",
                                 user="dbmasteruser",         
                                 password="ConsultIT1!", 
                                 database="dbmaster",
                                 port="3306")  
    print("Connected to MySql DB", mySQLCon.get_server_info())
    cur=mySQLCon.cursor()
    query=("select DATETIMECREATED,CAMERAID,FACEIDAWS,PHOTOFILENAME from GEYE_CAMERAFACESLOG")
    df=pd.read_sql(query, mySQLCon)
    # cur.execute(query)
    df1=df.to_excel("output.xlsx")
    print("Done")
    
    
except Exception as err:
    print("Not Connected", err)