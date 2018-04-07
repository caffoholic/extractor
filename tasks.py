import os, time
"""
Tasks to be executed when calling.
"""

def HideFiles(path):
    listFiles = os.listdir(path)

    for img in listFiles:
        print(img)
        isHidden = img[0:1]
        if(isHidden == '.'):
            print('File is already hidden')
        else:
            os.rename(path+img, path+"."+img)

def UnhideFiles(path):
    listFiles = os.listdir(path)

    for img in listFiles:
        time.sleep(0.15)
        print(img)
        isHidden = img[0:1]
        if(isHidden == '.'):        
            os.rename(path+img, path+img[1:])
        else:  
            print("File is already visible")

   
