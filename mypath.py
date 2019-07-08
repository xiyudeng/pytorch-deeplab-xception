class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            return 'dataloaders/datasets/pascal.py'  # folder that contains VOCdevkit/.
        elif dataset == 'sbd':
            return 'dataloaders/datasets/sbd.py'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return 'dataloaders/datasets/cityscapes.py'     # foler that contains leftImg8bit/
        elif dataset == 'coco':
            return 'dataloaders/datasets/coco.py' 
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
