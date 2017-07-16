from bs4 import BeautifulSoup
import urllib2
import os
import json


root_dir = os.path.dirname(os.path.realpath(__file__))

# set the dir where the images will be downloaded
dl_dir = root_dir + "/tf_images/pickup_trucks"

# Put the image query
query = "pickup trucks"

image_type = "photos"
query = query.split()
query = '+'.join(query)
url = "https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
print url

header = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'html.parser')

# contains the link for Large original images, type of  image
ActualImages = []

for a in soup.find_all("div", {"class": "rg_meta"}):
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    ActualImages.append((link, Type))

print "there are total", len(ActualImages), "images"

if not os.path.exists(dl_dir):
    os.mkdir(dl_dir)

if not os.path.exists(dl_dir):
    os.mkdir(dl_dir)

# write images to disk
for i, (img, Type) in enumerate(ActualImages):
    try:
        req = urllib2.Request(img, headers={"User-Agent": header})
        raw_img = urllib2.urlopen(req).read()

        cntr = len([i for i in os.listdir(dl_dir) if image_type in i]) + 1
        print cntr

        if len(Type) == 0:
            f = open(os.path.join(dl_dir, image_type + "_" + str(cntr) + ".jpg"), 'wb')
        else:
            if "jpg" not in Type:
                print "skipping non jpg images"
                continue
            else:
                f = open(os.path.join(dl_dir, image_type + "_" + str(cntr) + "." + Type), 'wb')

        f.write(raw_img)
        f.close()
    except Exception as e:
        print "could not load : " + img
        print e

