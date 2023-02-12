# from torchvision.datasets import CIFAR10









def cifar10_unpickle(path:str="datasets/cifar10/cifar-10-batches-py", pickle_file:str="all"):
    """Unpickle the CIFAR-10 dataset.

    Args:
        path (str, optional): Path of the CIFAR-10 directory. Defaults to "datasets/cifar10/cifar-10-batches-py".
        pickle_file (str, optional): The pickle file to be handled, the default value "all" will handle all pickle files. Defaults to "all".

    Returns:
        unpickle_dicts: If pickle_file is set to "all", a list of dictionaries will be returned. Otherwise, only a dictionary will be returned.
        Keys and values in each unpickle_dict:
        - b'batch_label': the name of the batch, e.g. b'training batch 1 of 5'.
        - b'labels': the labels of the batch data, e.g. 0, 2, 1, etc..
        - b'data': a numpy.ndarray object (shape (10000, 3072)) containing the batch data.
            Each row respresents a RGB image, the first 1024 enrtries for Red color, the next two 1024 entries are for Green and Blue. 
        - b'filenames': the file names of the batch data, e.g. b'tabby_s_002228.png'.
    """
    import pickle
    import glob
    
    if pickle_file == "all":
        pattern = path + "/" + "*batch*"
        pickle_batches = glob.glob(pattern)
        unpickle_dicts = []
        for batch in pickle_batches:
            with open(batch, "rb") as f:
                unpickle_dict = pickle.load(f, encoding="bytes")
                unpickle_dicts.append(unpickle_dict)
        return unpickle_dicts
    else:
        pickle_path = path + "/" + pickle_file
        with open(pickle_path, "rb") as f:
            unpickle_dict = pickle.load(f, encoding="bytes")
        return unpickle_dict


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    L = cifar10_unpickle(pickle_file="data_batch_1")
    img = L[b'data'][14].reshape(32, 32, 3, order="F")
    fig, ax = plt.subplots()
    ax.imshow(img)
    fig.savefig("img.png")
    plt.show()