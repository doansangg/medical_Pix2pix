import os.path
from data.base_dataset import BaseDataset, get_params, get_transform, normalize
from data.image_folder import make_dataset,delete_random_elems
from PIL import Image

class AlignedDataset(BaseDataset):
    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot    
        self.dir_A=opt.label_image
        self.A_paths = make_dataset(self.dir_A)
        len_A=len(self.A_paths)
        ### input B (real images)
        #if opt.isTrain or opt.use_encoded_image:
            # dir_B = '_B' if self.opt.label_nc == 0 else '_img'
            # self.dir_B = os.path.join(opt.dataroot, opt.phase + dir_B)  
        self.dir_B=opt.real_image
        self.B_paths = sorted(make_dataset(self.dir_B))
        len_B=len(self.B_paths)
        k=len_B-len_A
        if k>0:
            delete_random_elems(self.B_paths,k)
        if k<0:
            delete_random_elems(self.A_paths,abs(k))

        self.dataset_size = len(self.A_paths) 
      
    def __getitem__(self, index):        
        ### input A (label maps)
        A_path = self.A_paths[index]              
        A = Image.open(A_path)        
        params = get_params(self.opt, A.size)
        # if self.opt.label_nc == 0:
        transform_A = get_transform(self.opt, params)
        A_tensor = transform_A(A.convert('RGB'))
        # else:
        #     transform_A = get_transform(self.opt, params, method=Image.NEAREST, normalize=False)
        #     A_tensor = transform_A(A) * 255.0

        #B_tensor = inst_tensor = feat_tensor = 0
        ### input B (real images)
        #if self.opt.isTrain or self.opt.use_encoded_image:
        B_path = self.B_paths[index]   
        B = Image.open(B_path).convert('RGB')
        transform_B = get_transform(self.opt, params)      
        B_tensor = transform_B(B)

        ### if using instance maps        
        # if not self.opt.no_instance:
        #     inst_path = self.inst_paths[index]
        #     inst = Image.open(inst_path)
        #     inst_tensor = transform_A(inst)

        #     if self.opt.load_features:
        #         feat_path = self.feat_paths[index]            
        #         feat = Image.open(feat_path).convert('RGB')
        #         norm = normalize()
        #         feat_tensor = norm(transform_A(feat))                            

        input_dict = {'label': A_tensor,'image': B_tensor, 'path': A_path}

        return input_dict

    def __len__(self):
        return len(self.A_paths) // self.opt.batchSize * self.opt.batchSize

    def name(self):
        return 'AlignedDataset'