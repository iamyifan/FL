def my_dataloader(configs):
    from torchvision import transforms
    from torchvision.datasets import CIFAR10
    from torch.utils.data import DataLoader, random_split

    transform = transforms.Compose([
        transforms.ToTensor(),  # comvert the image to tensor so that it can work with torch
        transforms.Normalize((0.491, 0.482, 0.446),
                             (0.247, 0.243, 0.261))  # Normalize all the images
    ])

    num_clients = configs["client_configs"]["num_clients"]
    batch_size = 32

    cifar10 = CIFAR10("datasets/cifar10/",
                      train=True,
                      transform=transform,
                      download=False)
    # print(len(cifar10))
    splited_cifar10 = random_split(
        cifar10, lengths=[int(len(cifar10)/num_clients) for _ in range(num_clients)])
    dataloaders = [DataLoader(d, batch_size=batch_size, shuffle=True)
                   for d in splited_cifar10]

    return dataloaders


if __name__ == "__main__":
    def load_config(config_path: str):
        import json
        configs = {}
        with open(config_path) as f:
            configs = json.load(f)
        return configs
    configs = load_config("src/configs/fedavg/fedavg.json")
    dl = my_dataloader(configs)
    print(dl)
