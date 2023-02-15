def my_resnet18(weights='DEFAULT'):
    # import timm
    # return timm.create_model('resnet18', pretrained=True)
    from torchvision.models import resnet18
    return resnet18(weights=weights)


if __name__ == "__main__":
    from torchsummary import summary
    resnet18 = my_resnet18()
    print(summary(resnet18, input_size=(3, 32, 32)))