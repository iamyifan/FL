from src.utils.builder.fedavg import fedavg_api_builder

api = fedavg_api_builder("src/configs/fedavg/fedavg.json")
api.run()