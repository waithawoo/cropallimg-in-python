import os
import glob  # pip install glob2
from PIL import Image  # pip install Pillow
from pyfiglet import Figlet  # pip install pyfiglet

try:
    custom_fig = Figlet(font='standard')

    def getDirandFiletype():
        global img_dir, outpath, filenames

        print("Please enter Your Images Path.\n\neg:D:\Download\jaffedbase\n\n########################################")
        img_dir = input("What is your image directory path : ")
        outpath = input("What is your output path where to be saved : ")
        while(outpath == img_dir):
            print('Enter a different path with the image directory!!')
            outpath = input("What is your output path where to be saved : ")

        filetype = input("Enter file type (eg: png) : ")
        data_path = os.path.join(img_dir)
        # read all files in the path mentioned
        filenames = glob.glob(data_path + "/*." + filetype)
        processed = 0
        for file in filenames:
            img = Image.open(str(file))
            width, height = img.size
            print("Dimension of source images : "+width+"x"+height)
            processed += 1
            if processed >= 1:
                break 

        
    def getCoordinate():
        global left, top, right, bottom, img
        left = int(input("Enter left coordinate : "))  # 50
        top = int(input("Enter top coordinate : "))  # 50
        right = int(input("Enter right coordinate : "))  # 190
        bottom = int(input("Enter bottom coordinate : "))  # 235
    
    def main():
        getDirandFiletype()
        getCoordinate()
        for x in filenames:
            name = x.replace(img_dir, '')
            img = Image.open(str(x))
            region = img.crop((left, top,right, bottom))
            region.save(outpath + name)
        print(custom_fig.renderText('Done Image Cropping!'))
    main()
except SystemError:
    print("Sorry Buddy. Your Coordinates are invalid. Plese Check Coordinates Again!")
except ValueError:
    print("Please use Only Numbers for Coordinates!")
