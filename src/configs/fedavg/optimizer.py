def my_optimizer(client):
    from torch.optim import SGD
    return SGD(client.parameters(), lr=1.0)