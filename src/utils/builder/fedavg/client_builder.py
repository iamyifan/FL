def fedavg_client_builder(configs, *args, **kwargs):
    """Ref: https://github.com/Koukyosyumei/AIJack/blob/main/src/aijack/collaborative/fedavg/client.py
    """
    from aijack.collaborative.fedavg import FedAVGClient
    from ..loader import load_model, load_optimizer, load_dataloader

    clients, optimizers, dataloaders = [], [], []

    client_configs = configs["client_configs"]
    server_configs = configs["server_configs"]
    other_configs = configs["other_configs"]

    optimizer = load_optimizer(client_configs["local_optimizer_path"],
                               client_configs["local_optimizer_func_name"])
    dataloader = load_dataloader(client_configs["local_dataloader_path"],
                                 client_configs["local_dataloader_func_name"])
    
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
        model = load_model(server_configs["global_model_path"],
                           server_configs["global_model_func_name"])
        client = FedAVGClient(model=model.to(device),
                              user_id=i,
                              lr=lr,
                              send_gradient=send_gradient,
                              optimizer_type_for_global_grad=optimizer_type_for_global_grad,
                              server_side_update=server_side_update,
                              optimizer_kwargs_for_global_grad=optimizer_kwargs_for_global_grad,
                              device=device)
        clients.append(client)
        optimizers.append(optimizer(client))
    
    dataloaders = dataloader(configs)

    return clients, optimizers, dataloaders
