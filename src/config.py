import yaml

train_dir = './data/train'
val_dir = './data/val'
test_dir = './data/test'
annotation_dir = './data/annotations'
chkpt_dir = './model_chkpt'
tensorboard_dir = './runs'
log_dir = './logs'

device = 'cuda'
cores = 2
classes = {
    '0': 'background',
    '1': 'split',
    '2': 'seed',
    '3': 'pod'
}
n_classes = 4
resize_to = 3000
n_epochs = 100
batch_size = 4
base_name = 'sainfoin_seed'
lr = 0.01
momentum = 0.8
gamma = 0.9


def parse_config(file_name):
   
    with open('model_config.yml', 'r') as f:
        conf = yaml.safe_load(f)

    train_dir = conf['directories']['train']
    val_dir = conf['directories']['val']
    test_dir = conf['directories']['test']
    annot_dir = conf['directories']['annotations']
    chkpt_dir = conf['directories']['checkpoints']
    try:
        tb_dir = conf['directories']['tensorboard']
    except KeyError as e:
        print(f"Key {e}not in configuration file keys. Assigning default value at './runs'")
        tb_dir = './runs'
    try:
        log_dir = conf['directories']['logs']
    except KeyError as e:
        print(f"Key {e} not in configuration file keys. Assigning default value at './logs'")
        log_dir = './logs'

    device = conf['training']['device']
    cores = conf['training']['cores']
    classes = conf['training']['classes']
    n_classes = conf['training']['n_classes']
    resize_to = conf['training']['resize_to']

    n_epochs = conf['settings']['n_epochs']
    batch_size = conf['settings']['batch_size']
    model_base_name = conf['settings']['model_name']
    lr = conf['settings']['lr']
    momentum = conf['settings']['momentum']
    gamma = conf['settings']['gamma']


    conf_settings = tuple([train_dir, 
                          val_dir, 
                          test_dir, 
                          annot_dir, 
                          chkpt_dir,
                          tb_dir, 
                          log_dir, 
                          device, 
                          cores, 
                          classes, 
                          n_classes, 
                          resize_to, 
                          n_epochs, 
                          batch_size, 
                          model_base_name, 
                          lr, 
                          momentum, 
                          gamma])
    
    return conf_settings
