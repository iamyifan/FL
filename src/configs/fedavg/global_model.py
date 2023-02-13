import timm

def create_resnet18(pretrained=True):
    return timm.create_model('resnet18', pretrained=pretrained)

if __name__ == "__main__":
    create_resnet18()