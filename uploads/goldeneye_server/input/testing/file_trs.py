import os
import shutil

vids_path = "/home/sftpuser/bbf0a2f7"
dst = "/home/centos/goldeneye/uploads/bbf0a2f7/processing/video"

def move_files():
    try:
        count=0
        for filename in os.listdir(vids_path):
            src_path = os.path.join(vids_path, filename)
            dst_path = os.path.join(dst, filename)
            
            if os.path.isfile(src_path) and filename.endswith(".mp4"):
                shutil.move(src_path, dst_path)
                count+=1
                # print(f"{filename} moved successfully.")
            else:
                print(f"{filename} is not available or not an MP4 file.")
                
        print(f"{count} videos moved successfully.")
        
    except Exception as e:
        print("File Not Found")

move_files()
