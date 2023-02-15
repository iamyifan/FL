def my_loss(pred, target):
    from torch.nn.functional import nll_loss
    return nll_loss(pred, target)


if __name__ == "__main__":
    my_loss()