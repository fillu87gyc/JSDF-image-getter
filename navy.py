import urllib.request
import os
import time
name = 'name'
num = 0
target_dir = "./Navy/"
url = ''
path = ''
flg = False
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
shiptype = input("護衛艦:dd / 潜水艦:ss / 掃海艦:mso /ミサイル艦:pg /練習艦:tv /\n>>")
if not os.path.exists(target_dir+shiptype+"/"):
    os.mkdir(target_dir + shiptype + "/")
while name != "end":
    name = input('name :')
    num = int(input("start num: "))
    locate = "http://www.mod.go.jp/msdf/formal/gallery/ships/" + \
        shiptype + "/" + name + "/img/"
    if not os.path.exists(target_dir+shiptype + "/" + name+"/"):
        os.mkdir(target_dir + shiptype + "/" + name + "/")
    for i in range(0, 100):
        if flg:
            flg = False
            break
        if not os.path.exists(target_dir+shiptype+"/"+name+"/"+str(i+num)):
            os.mkdir(target_dir+shiptype+"/"+name+"/"+str(i+num))
        for j in range(1, 50):

            if j < 10:
                url = locate + str(i + num) + '_0' + str(j) + 'l.jpg'
            else:
                url = locate + str(i+num) + '_' + str(j) + 'l.jpg'
            path = target_dir+shiptype+"/"+name + \
                "/"+str(i+num)+"/"+str(j)+".jpg"
            try:
                if not os.path.exists(path):
                    urllib.request.urlretrieve(url, path)
                    print(str(j)+":Downloading "+url)
                    time.sleep(0.2)
            except urllib.error.URLError:
                print("もうないのでbreak")
                is_exist_path = target_dir + shiptype + "/" + name + "/"
                # debug = os.listdir(is_exist_path)
                if not os.path.exists(is_exist_path + str(num) + "/1.jpg"):
                    os.rmdir(target_dir+shiptype+"/"+name+"/"+str(num))
                    os.rmdir(target_dir + shiptype + "/" + name + "/")
                    flg = True
                    print("間違った艦名を入力したと思われます 画像が見つかりません")
                break
        try:
            os.rmdir(target_dir+shiptype+"/"+name+"/"+str(i+num))
            print("ファイルがないので消す")
            break
        except:
            print("ディレクトリがない or emptyでない")
