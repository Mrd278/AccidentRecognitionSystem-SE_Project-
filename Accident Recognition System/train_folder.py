import os

path = 'dataset/'

imglist = os.listdir('images')

print(imglist)

textfile = open('train.txt', 'w')

for img in imglist:
    imgpath = path + img + '\n'
    textfile.write(imgpath)
