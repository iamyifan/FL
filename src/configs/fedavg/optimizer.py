def my_optimizer(client):
    from torch.optim import SGD
    return SGD(client.parameters(), lr=0.01)