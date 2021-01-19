import os
import glob #pip install glob2
import re
import numpy as np
from PIL import Image #pip install Pillow
from pyfiglet import Figlet #pip install pyfiglet


custom_fig = Figlet(font='standard')

print("Please enter Your Images Path.\n\nPlease use Path Name like this (with double \\\) \n\neg:D:\\\Download\\\jaffedbase\n\n########################################")

img_dir = input("What is your image directory path : ")
outpath = input("What is your output path where to be saved : ")
filetype = input("Enter file type : ")

print("Recommended for jaffedbase : x1=50, y1=50, x2=190, y2=235\n")
x1_coordinate = int(input("Enter x1 coordinate : "))#50
y1_coordinate = int(input("Enter y1 coordinate : "))#50
x2_coordinate = int(input("Enter x2 coordinate : "))#190
y2_coordinate = int(input("Enter y2 coordinate : "))#235
data_path = os.path.join(img_dir)
filenames = glob.glob(data_path + "/*." + filetype) #read all files in the path mentioned

for x in filenames:
    print(x)
    name = (x.replace(img_dir, ''))
    print(name)
    img = Image.open(str(x))
    region = img.crop((x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate))
    region.save(outpath  + name )
print(custom_fig.renderText('Hey My Baby. Your Image Cropping is Done with My LOVE!'))
