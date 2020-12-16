import predictor as pd
from datetime import date


if __name__ == '__main__':
    # Factory method and Prototype
    print('-------------Factory method and Prototype----------------------')
    client1 = pd.Manager(pd.DataPredictionCreator())
    print('-----------First client demo-------------------')
    client1.use_factory([1,2,3])

    client2 = pd.Manager(pd.DataHistoryCreator())
    print('-----------Second client demo-------------------')
    client1.use_factory([4,5,6])

    # Singleton
    print('---------------Singleton---------------------')
    vault1 = pd.data.PredictionVault(1)
    vault2 = pd.data.PredictionVault(2)
    print(f"id's: {id(vault1)}, {id(vault2)}")
    print(f"values: {vault1.data}, {vault2.data}")

    # Abstract Factory
    print('------------Abstract Factory----------------')
    factory1 = pd.MacDataFactory()
    factory2 = pd.WindowsDataFactory()

    client = pd.Manager(factory1)
    print('-----------First factory demo-------------------')
    client.use_abs_factory()

    client = pd.Manager(factory2)
    print('-----------Second factory demo-------------------')
    client.use_abs_factory()





