def _load_model(module_path: str, model_func_name: str):
    from importlib.machinery import SourceFileLoader
    module_name = module_path.split("/")[-1]
    module = SourceFileLoader(module_name, module_path).load_module()
    model = eval("module.{}()".format(model_func_name))
    return model


def _load_optimizer(optimizer_path: str, optimizer_func_name: str):
    from importlib.machinery import SourceFileLoader
    module_name = optimizer_path.split("/")[-1]
    module = SourceFileLoader(module_name, optimizer_path).load_module()
    optimizer = eval("module.{}()".format(optimizer_func_name))
    return optimizer


def _load_config(fedavg_config_path: str = "src/configs/fedavg/fedavg.json"):
    import json
    configs = {}
    with open(fedavg_config_path) as f:
        configs = json.load(f)
    return configs


def fedavg_client_builder(fedavg_client_class, configs):
    """Create a list of FedAvg clients and a list of optimizers for each client.

    Args:
        fedavg_client_class (FedAVGClient):
            https://github.com/Koukyosyumei/AIJack/blob/main/src/aijack/collaborative/fedavg/client.py
        configs (dict): A dictionary of configs from a json file.

    Returns:
        A list of FedAvg lients and a list of optimizers for each client are returned.
    """

    clients = []

    client_configs = configs["client_configs"]
    server_configs = configs["sever_configs"]
    other_configs = configs["other_configs"]

    model = _load_model(
        server_configs["global_model_path"], server_configs["global_model_func_name"])
    device = other_configs["device"]

    ##### DO NOT MODIFY #####
    send_gradient = False      # update model with aggregated params, default True
    server_side_update = True  # default True
    ##### DO NOT MODIFY #####

    ##### NOT USED IN PARAMS-UPDATED MODE, SET AS DEFAULT VALUE IN AIJACK #####
    lr = 0.1
    optimizer_type_for_global_grad = "sgd"
    optimizer_kwargs_for_global_grad = {}
    ##### NOT USED IN PARAMS-UPDATED MODE, SET AS DEFAULT VALUE IN AIJACK #####

    for i in range(client_configs["num_clients"]):
        client = fedavg_client_class(model=model,
                                     user_id=i,
                                     lr=lr,
                                     send_gradient=send_gradient,
                                     optimizer_type_for_global_grad=optimizer_type_for_global_grad,
                                     server_side_update=server_side_update,
                                     optimizer_kwargs_for_global_grad=optimizer_kwargs_for_global_grad,
                                     device=device)
        clients.append(client)

    return clients


def fedavg_server_builder(fedavg_server_class, configs):
    """Create a FedAvg server.

    Args:
        fedavg_sever_class (FedAVGServer):
            https://github.com/Koukyosyumei/AIJack/blob/main/src/aijack/collaborative/fedavg/server.py
        configs (dict): A dictionary of configs from a json file.

    Returns:
        server (FedAVGServer): A FedAvg server.
    """

    client_configs = configs["client_configs"]
    server_configs = configs["sever_configs"]
    other_configs = configs["other_configs"]

    # a list of client's IDs
    clients = list(range(client_configs["num_clients"]))
    global_model = _load_model(
        server_configs["global_model_path"], server_configs["global_model_func_name"])
    server_id = server_configs["server_id"]
    device = other_configs["device"]

    ##### DO NOT MODIFY #####
    server_side_update = True  # default True
    ##### DO NOT MODIFY #####

    ##### NOT USED IN PARAMS-UPDATED MODE, SET AS DEFAULT VALUE IN AIJACK #####
    lr = 0.1
    optimizer_type = "sgd"
    optimizer_kwargs = {}
    ##### NOT USED IN PARAMS-UPDATED MODE, SET AS DEFAULT VALUE IN AIJACK #####

    server = fedavg_server_class(
        clients=clients,
        global_model=global_model,
        server_id=server_id,
        lr=lr,
        optimizer_type=optimizer_type,
        server_side_update=server_side_update,
        optimizer_kwargs=optimizer_kwargs,
        device=device
    )

    return server


if __name__ == "__main__":
