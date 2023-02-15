def fedavg_server_builder(configs, *args, **kwargs):
    """Ref: https://github.com/Koukyosyumei/AIJack/blob/main/src/aijack/collaborative/fedavg/server.py
    """
    from aijack.collaborative.fedavg import FedAVGServer
    from ..loader import load_model

    server_configs = configs["server_configs"]
    other_configs = configs["other_configs"]

    clients = kwargs["clients"]  # passed from FedAVGAPI
    global_model = load_model(server_configs["global_model_path"],
                              server_configs["global_model_func_name"])
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

    server = FedAVGServer(
        clients=clients,
        global_model=global_model.to(device),
        server_id=server_id,
        lr=lr,
        optimizer_type=optimizer_type,
        server_side_update=server_side_update,
        optimizer_kwargs=optimizer_kwargs,
        device=device
    )

    return server