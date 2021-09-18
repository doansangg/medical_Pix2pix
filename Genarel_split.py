import os

from PIL.Image import Image
train=open("path_data/input.txt","w+")
real_input=open("path_data/real_ouput.txt","w+")
#path fodel genarel:
path_image="../labeled-images/upper-gi-tract/anatomical-landmarks"
#name path folder => GEN
name_GEN='z-line'
#number images GEN
number_GEN=1000
#gen sample image?
sample=False
folder=os.listdir(path_image)
folder.remove(name_GEN)
folder.insert(0, name_GEN)
for count,fd in enumerate(folder):
    len_data=len(os.listdir(path_image+'/'+name_GEN))
    if number_GEN>=len_data:
        number_GEN=len_data
    if fd==name_GEN:
        for sang,i in enumerate(os.listdir(path_image+'/'+fd)):
            image=path_image+'/'+fd+'/'+i
            if os.path.exists(image):
                if sang <= number_GEN:
                    train.write(image+"\n")
    if sample:
        if fd==name_GEN:
            for sang,i in enumerate(os.listdir(path_image+'/'+fd)):
                image=path_image+'/'+fd+'/'+i
                if os.path.exists(image):
                    if sang <= number_GEN:
                        real_input.write(image+'\n')
        break
    if fd!=name_GEN:
        for sang,i in enumerate(os.listdir(path_image+'/'+fd)):
            image=path_image+'/'+fd+'/'+i
            if os.path.exists(image):
                if sang < number_GEN:
                    real_input.write(image+"\n")