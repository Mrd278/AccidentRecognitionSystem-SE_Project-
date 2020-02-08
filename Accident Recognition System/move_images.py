import os

folders = ['Accident_Images']
path = r'D:\\Mridul\\Machine Learning\\Software_Engineering_Project\\Accident Recognition System\\images'


n = 63
for folder in folders:
    for image in os.scandir(folder):
        n+=1
        os.rename(image.path, os.path.join(path, '{:06}.jpg'.format(n)))
