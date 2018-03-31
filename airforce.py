import urllib.request
import os
import time
name = [
    "F-15/",
    "F-35/",
    "F-2/",
    "F-4/",
    "RF-4E/",
    "E-767/",
    "E-2C/",
    "C-1/",
    "C-2/",
    "C-130H/",
    "B-747/",
    "CH-47J/",
    "KC-767/",
    "U-125A/",
    "UH-60J/",
    "U-4/",
    "U-125/",
    "YS-11FC/",
    "T-4/",
    "T-7/",
    "T-400/",
    "T-4_Blueimpulse/",
    "yuudoudan/",
    "Patriot/",
    "end"
]
target_dir = "./AirForce/"
url = ''
path = ''
# /todoroki/F_15/photo01.jpg
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
while name[0] != "end":
    locate = "http://www.mod.go.jp/asdf/equipment/all_equipment/" + \
        name[0]+"images/photo"
    if not os.path.exists(target_dir+name[0]):
        os.mkdir(target_dir + name[0])
    for i in range(1, 50):
        if i < 10:
            url = locate + '0' + str(i) + '.jpg'
        else:
            url = locate + str(i) + '.jpg'
        path = target_dir+name[0]+str(i)+".jpg"
        try:
            if not os.path.exists(path):
                urllib.request.urlretrieve(url, path)
                print(str(i)+":Downloading "+url)
                time.sleep(1)
        except urllib.error.URLError:
            print("もうないのでbreak")
            name.pop(0)
            break
print("正常終了...")
time.sleep(5)
