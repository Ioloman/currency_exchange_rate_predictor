**-------------Factory method and Prototype----------------------**

<Manager>_<-->_<2019478803312>:<__init__>[<-->] -- method

**-----------First client demo-------------------**

<Manager>_<Client (Factory method)>_<2019478803312>:<use_factory>[<-->] -- method

<DataPredictionCreator>_<Prediction factory (Factory method)>_<2019478803888>:<create_data>[<creates concrete object>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478803168>:<__init__>[<-->] -- method

<Manager>_<Client (Factory method)>_<2019478803312>:<use_object>[<-->] -- method

<DataPrediction>_<Prototype>_<2019478803168>:<__copy__>[<shallow copy>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478806432>:<__init__>[<-->] -- method

<DataPrediction>_<Prototype>_<2019478803168>:<__deepcopy__>[<deep copy>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478806048>:<__init__>[<-->] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478803168>:<extend>[<-->] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478803168>:<save>[<-->] -- method

<Manager>_<-->_<2019478803216>:<__init__>[<-->] -- method

**-----------Second client demo-------------------**

<Manager>_<Client (Factory method)>_<2019478803312>:<use_factory>[<-->] -- method

<DataPredictionCreator>_<Prediction factory (Factory method)>_<2019478803888>:<create_data>[<creates concrete object>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478806192>:<__init__>[<-->] -- method

<Manager>_<Client (Factory method)>_<2019478803312>:<use_object>[<-->] -- method

<DataPrediction>_<Prototype>_<2019478806192>:<__copy__>[<shallow copy>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478803648>:<__init__>[<-->] -- method

<DataPrediction>_<Prototype>_<2019478806192>:<__deepcopy__>[<deep copy>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478855792>:<__init__>[<-->] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478806192>:<extend>[<-->] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478806192>:<save>[<-->] -- method

**---------------Singleton---------------------**

<SingletonMeta>_<Singleton metaclass (Singleton)>_<2019469103872>:<__call__>[<managing instances>] -- method

<PredictionVault>_<Singleton itself (Singleton)>_<2019478806432>:<__init__>[<-->] -- method

<SingletonMeta>_<Singleton metaclass (Singleton)>_<2019469103872>:<__call__>[<managing instances>] -- method

id's: 2019478806432, 2019478806432

values: 1, 1

**------------Abstract Factory----------------**

<MacDataFactory>_<Factory (Abstract factory)>_<2019478806192>:<__init__>[<factory initiation>] -- method

<WindowsDataFactory>_<Factory (Abstract factory)>_<2019478805712>:<__init__>[<factory initiation>] -- method

<Manager>_<-->_<2019478855792>:<__init__>[<-->] -- method

**-----------First factory demo-------------------**

<Manager>_<Client (Abstract factory)>_<2019478855792>:<use_abs_factory>[<-->] -- method

<MacDataFactory>_<Factory (Abstract factory)>_<2019478806192>:<create_history_data>[<create history data>] -- method

<MacDataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856272>:<__init__>[<-->] -- method

<Manager>_<Client (Factory method)>_<2019478855792>:<use_object>[<-->] -- method

<MacDataHistory>_<Prototype>_<2019478856272>:<__copy__>[<shallow copy>] -- method

<MacDataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856512>:<__init__>[<-->] -- method

<MacDataHistory>_<Prototype>_<2019478856272>:<__deepcopy__>[<deep copy>] -- method

<MacDataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856032>:<__init__>[<-->] -- method

<MacDataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856272>:<extend>[<-->] -- method

<MacDataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856272>:<save>[<-->] -- method

<MacDataFactory>_<Factory (Abstract factory)>_<2019478806192>:<create_prediction_data>[<create prediction data>] -- method

<MacDataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856032>:<__init__>[<-->] -- method

<Manager>_<Client (Factory method)>_<2019478855792>:<use_object>[<-->] -- method

<MacDataPrediction>_<Prototype>_<2019478856032>:<__copy__>[<shallow copy>] -- method

<MacDataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856272>:<__init__>[<-->] -- method

<MacDataPrediction>_<Prototype>_<2019478856032>:<__deepcopy__>[<deep copy>] -- method

<MacDataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856464>:<__init__>[<-->] -- method

<MacDataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856032>:<extend>[<-->] -- method

<MacDataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856032>:<save>[<-->] -- method

<Manager>_<-->_<2019478856032>:<__init__>[<-->] -- method

**-----------Second factory demo-------------------**

<Manager>_<Client (Abstract factory)>_<2019478856032>:<use_abs_factory>[<-->] -- method

<WindowsDataFactory>_<Factory (Abstract factory)>_<2019478805712>:<create_history_data>[<create history data>] -- method

<DataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478855792>:<__init__>[<-->] -- method

<Manager>_<Client (Factory method)>_<2019478856032>:<use_object>[<-->] -- method

<DataHistory>_<Prototype>_<2019478855792>:<__copy__>[<shallow copy>] -- method

<DataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856464>:<__init__>[<-->] -- method

<DataHistory>_<Prototype>_<2019478855792>:<__deepcopy__>[<deep copy>] -- method

<DataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478856368>:<__init__>[<-->] -- method

<DataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478855792>:<extend>[<-->] -- method

<DataHistory>_<Created by factory (Factory method/Abstract factory)>_<2019478855792>:<save>[<-->] -- method

<WindowsDataFactory>_<Factory (Abstract factory)>_<2019478805712>:<create_prediction_data>[<create prediction data>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856368>:<__init__>[<-->] -- method

<Manager>_<Client (Factory method)>_<2019478856032>:<use_object>[<-->] -- method

<DataPrediction>_<Prototype>_<2019478856368>:<__copy__>[<shallow copy>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478855792>:<__init__>[<-->] -- method

<DataPrediction>_<Prototype>_<2019478856368>:<__deepcopy__>[<deep copy>] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856512>:<__init__>[<-->] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856368>:<extend>[<-->] -- method

<DataPrediction>_<Created by factory (Factory method/Abstract factory)>_<2019478856368>:<save>[<-->] -- method


Process finished with exit code 0