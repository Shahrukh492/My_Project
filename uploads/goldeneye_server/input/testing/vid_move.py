import os
from time import sleep

vids_path = '/tmp/geyeftp/3c01cc89'
target_path1 = '/home/centos/goldeneye/uploads/3c01cc89/processing/video'
target_path2 = '/home/centos/goldeneye/uploads/3c01cc89/subprocessing/video'
videos = []
vid_name = []
targ_vid = []

for filename in os.listdir(vids_path):
    if filename.endswith('.mp4'):
        vid_path = os.path.join(vids_path, filename)
        videos.append(vid_path)
        vid_name.append(filename)

def tagDect():
    targ_vid.clear()
    for filename in os.listdir(target_path1):
        if filename.endswith('.mp4'):
            targ_vid.append(filename)


def resetDect():
    sleep(40)
    videos1 = []
    vid_name1 = []

    for filename in os.listdir(vids_path):
        if filename.endswith('.mp4'):
            vid_path = os.path.join(vids_path, filename)
            videos1.append(vid_path)
            vid_name1.append(filename)
    videos.clear()
    vid_name.clear()
    videos.extend(videos1)
    vid_name.extend(vid_name1)


tagDect()
for i, vid in enumerate(videos):

    if len(targ_vid) == 0:

        os.replace(vid, f'{target_path1}/{vid_name[i]}')
	
    else:

        os.replace(vid, f'{target_path2}/{vid_name[i]}')
	
print("Videos send Completed")

