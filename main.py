import predictor as pd
from datetime import date


if __name__ == '__main__':
    # proxy
    print('------------Proxy----------------')
    real = pd.DataVault()
    proxy = pd.DataVaultProxy(real)
    result = proxy.get_data(('rub', 'usd'), date(2020, 1, 1), 'day', date(2020, 1, 31))

    # delegation
    print('-----------Delegation-------------')
    visualizers = [pd.Visualizer1(), pd.Visualizer2()]
    predictors = [pd.Predictor1(), pd.Predictor2()]

    manager1 = pd.Manager(predictors[0], visualizers[1])
    manager2 = pd.Manager(predictors[1], visualizers[0])

    manager1.predict(pd.Data())
    manager1.show(pd.Data(), pd.Data())

    manager2.predict(pd.Data())
    manager2.show(pd.Data(), pd.Data())

