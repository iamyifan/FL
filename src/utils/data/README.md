# Downloading Dataset

## CIFAR-10
`CIFAR-10` consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

Read more information about the dataset in Alex Krizhevsky's [page](https://www.cs.toronto.edu/~kriz/cifar.html).

The function `download_dataset()` in `download.py` uses `wget` command to download the dataset recource.



## ImageNet 1000 (mini)
`ImageNet 1000 (mini)` is download from the [dataset](https://www.kaggle.com/datasets/ifigotin/imagenetmini-1000) in kaggle.

For accessing `kaggle API` to download the dataset, please:
1. Download `kaggle API`: \
   `pip install --user kaggle`
2. Setup `kaggle API`: \
   Navigate to your kaggle page: \
   `https://www.kaggle.com/<USER_NAME>/account` \
   Go to the API section and create a new API token, then a `kaggle.json` file will be created and downloaded. \
   Make a directory at root `~/.kaggle`, then save `kaggle.json` under `~/.kaggle`.

Read more `kaggle API` guide from the [reference](https://www.endtoend.ai/tutorial/how-to-download-kaggle-datasets-on-ubuntu/).