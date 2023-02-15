import os

def download_dataset(name:str="cifar10", path:str=".", unzip:bool=True, traverse:bool=False):
    full_path = path + "/" + name
    os.system("mkdir -p {}".format(full_path))

    if name == "cifar10":
        url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
        os.system("wget -P {} {}".format(full_path, url))
        if unzip:
            file_path = full_path + "/" + "cifar-10-python.tar.gz"
            os.system("tar -xf {} -C {}".format(file_path, full_path))
    elif name == "imagenet1000":
        kaggle_repo = "ifigotin/imagenetmini-1000"
        os.chdir(full_path)
        os.system("kaggle datasets download {}".format(kaggle_repo))
        if unzip:
            os.system("unzip imagenetmini-1000.zip")
    else:
        print("Invalid dataset name.")
        return
    
    if traverse:
        for dir_path, dir_names, data_names in os.walk(full_path):
            print("In {}, there are {} folders and {} files.".format(dir_names, len(dir_names), len(data_names)))


if __name__ == "__main__":
    # download_dataset(name="cifar10", path="datasets", unzip=True, traverse=True)
    download_dataset(name="imagenet1000", path="datasets", unzip=True, traverse=True)