def fedavg_api_builder(configs_path):
    """Ref: https://github.com/Koukyosyumei/AIJack/blob/main/src/aijack/collaborative/fedavg/api.py
    """
    from aijack.collaborative.fedavg import FedAVGAPI
    from ..loader import load_config, load_loss
    from .client_builder import fedavg_client_builder
    from .server_builder import fedavg_server_builder

    configs = load_config(configs_path)

    client_configs = configs["client_configs"]
    server_configs = configs["server_configs"]
    other_configs = configs["other_configs"]

    clients, local_optimizers, local_dataloaders = fedavg_client_builder(
        configs)
    server = fedavg_server_builder(configs, clients=clients)
    criterion = load_loss(other_configs["training_loss_path"],
                          other_configs["training_loss_func_name"])
    num_communication = server_configs["num_communication"]
    local_epoch = client_configs["num_epochs"]
    device = other_configs["device"]
    def custom_action(x): return x  # TODO
    ##### DO NOT MODIFY #####
    use_gradients = False  # upgrade model with clients' params
    ##### DO NOT MODIFY #####

    api = FedAVGAPI(
        server=server,
        clients=clients,
        criterion=criterion,
        local_optimizers=local_optimizers,
        local_dataloaders=local_dataloaders,
        num_communication=num_communication,
        local_epoch=local_epoch,
        use_gradients=use_gradients,
        custom_action=custom_action,
        device=device
    )

    return api