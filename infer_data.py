from options.train_options import TrainOptions
import torch
import torchvision.utils as vutils
import time
from data.data_loader import CreateDataLoader
opt = TrainOptions().parse()
data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
for i, data in enumerate(dataset, start=0):
    print(data['label'].shape)
    #break
    #vutils.save_image(data['inst'],'doansang.png')
    #time.sleep(1)
    #plt.show(data['image'][0])