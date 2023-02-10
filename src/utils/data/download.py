import os

def download_dataset(name:str="cifar10", path:str=""):
    url = ""
    if name == "cifar10":
        url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    elif name == "imagenet1000":
        url = "https://www.kaggle.com/datasets/ifigotin/imagenetmini-1000/download?datasetVersionNumber=1"
    else:
        print("Invalid dataset name.")
        return
    
    full_path = path + "/" + name
    dataset_path = full_path + "/" + name

    os.system("mkdir -p {}".format(dataset_path))
    os.system("wget -O {} {}".format(full_path, url))
    
