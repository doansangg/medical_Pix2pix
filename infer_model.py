from models.networks import define_G
from options.train_options import TrainOptions
import torch
opt = TrainOptions().parse()
netG_input_nc=3
netG=define_G(opt.output_nc, opt.feat_num, opt.nef, 'global', 
                                          opt.n_downsample_E, norm=opt.norm, gpu_ids=opt.gpu_ids)
input=torch.rand([1,3,352,352]).cuda()
isn=torch.randint(0, 1, (1,)).cuda()
print(netG(input).shape)