def load_config(config_path: str):
    import json
    configs = {}
    with open(config_path) as f:
        configs = json.load(f)
    return configs


def load_model(module_path: str, model_func_name: str):
    from copy import deepcopy
    from importlib.machinery import SourceFileLoader
    module_name = module_path.split("/")[-1]
    module = SourceFileLoader(module_name, module_path).load_module()
    model = eval("module.{}()".format(model_func_name))
    # return deepcopy(model)
    return model


def load_optimizer(optimizer_path: str, optimizer_func_name: str):
    from importlib.machinery import SourceFileLoader
    module_name = optimizer_path.split("/")[-1]
    module = SourceFileLoader(module_name, optimizer_path).load_module()
    optimizer_func = eval("module.{}".format(optimizer_func_name))
    return optimizer_func


def load_loss(loss_path: str, loss_func_name: str):
    from importlib.machinery import SourceFileLoader
    module_name = loss_path.split("/")[-1]
    module = SourceFileLoader(module_name, loss_path).load_module()
    loss_func = eval("module.{}".format(loss_func_name))
    return loss_func


def load_dataloader(dataloader_path: str, dataloader_func_name: str):
    from importlib.machinery import SourceFileLoader
    module_name = dataloader_path.split("/")[-1]
    module = SourceFileLoader(module_name, dataloader_path).load_module()
    dataloader_func = eval("module.{}".format(dataloader_func_name))
    return dataloader_func