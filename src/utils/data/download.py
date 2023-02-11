import os

def download_dataset(name:str="cifar10", path:str="."):
    url = ""
    if name == "cifar10":
        url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    elif name == "imagenet1000":
        url = "https://www.kaggle.com/datasets/ifigotin/imagenetmini-1000/download?datasetVersionNumber=1"
    else:
        print("Invalid dataset name.")
        return
    
    full_path = path + "/" + name
    os.system("mkdir -p {}".format(full_path))

    if name == "cifar10":
        os.system("wget -P {} {}".format(full_path, url))
        raw_file = full_path + "/" + "cifar-10-python.tar.gz"
        os.system("tar -xf {} -C {}".format(raw_file, full_path))
    elif name == "imagenet1000":
        os.chdir(full_path)
        os.system("kaggle datasets download ifigotin/imagenetmini-1000")
        os.system("unzip imagenetmini-1000.zip")
    

if __name__ == "__main__":
    download_dataset(name="cifar10", path="datasets")
    download_dataset(name="imagenet1000", path="datasets")