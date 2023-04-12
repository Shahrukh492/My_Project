import os
import shutil
  
# Path to the file/directory
src_path = "/home/sftpuser/3c01cc89"
dst_path = "/home/centos/goldeneye/uploads/3c01cc89/processing/video"


def move_file():
    try:
        list_of_files = filter( lambda x: os.path.isfile(os.path.join(src_path, x)),
                            os.listdir(src_path) )
        list_of_files = sorted( list_of_files,
                            key = lambda x: os.path.getctime(os.path.join(src_path, x))
                            )
        for file_path in list_of_files:
            new_src = os.path.join(src_path, file_path)
            new_dst = os.path.join(dst_path, file_path)
            #print(file_path)
            
            shutil.move(new_src, new_dst)
        print("Videos moves to Successfully")
            
        
    except Exception as e:
        print("File Not Available")

move_file()

