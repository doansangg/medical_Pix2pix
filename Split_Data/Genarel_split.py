import os
train=open("path_data/train.txt","w+")
val=open("path_data/val.txt","w+")
test=open("path_data/test.txt","w+")
path_image="../labeled-images/upper-gi-tract/anatomical-landmarks"
folder=os.listdir(path_image)
for count,fd in enumerate(folder):
    for sang,i in enumerate(os.listdir(path_image+'/'+fd)):
        image=path_image+'/'+fd+'/'+i
        string=image+"\t"+str(count)+"\n"
        if os.path.exists(image):
            if sang < 0.6* len(os.listdir(path_image+'/'+fd)):
                train.write(string)
            # if sang < 0.9*len(os.listdir(path_image+'/'+fd)) and sang >= 0.8* len(os.listdir(path_image+'/'+fd)):
            #     val.write(string)
            if sang >= 0.6*len(os.listdir(path_image+'/'+fd)) :
                test.write(string)