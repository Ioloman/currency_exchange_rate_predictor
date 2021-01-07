**Пример логов**

<Manager>_<client>_<1797883690864>:<__init__>[<-->] -- method

<DataExtractor>_<Main class (Strategy)>_<1797883672896>:<__init__>[<-->] -- method

<DataVaultProxy>_<Observer (Observer)>_<1797883672704>:<__init__>[<-->] -- method

<PredictEventManager>_<Event Manager (observer)>_<1797883672512>:<__init__>[<-->] -- method

**--------------------- Strategy -------------------------**

**need second source**

<Manager>_<client>_<1797883690864>:<extract_data>[<-->] -- method

<DataExtractor>_<Main class (Strategy)>_<1797883672896>:<set_strategy>[<setter>] -- method

<DataExtractor>_<Main class (Strategy)>_<1797883672896>:<extract_data>[<call strategy method>] -- method

<Strategy2>_<Strategy (Strategy)>_<1797883671936>:<extract_data>[<-->] -- method

**need first source**

<Manager>_<client>_<1797883690864>:<extract_data>[<-->] -- method

<DataExtractor>_<Main class (Strategy)>_<1797883672896>:<set_strategy>[<setter>] -- method

<DataExtractor>_<Main class (Strategy)>_<1797883672896>:<extract_data>[<call strategy method>] -- method

<Strategy1>_<Strategy (Strategy)>_<1797883672944>:<extract_data>[<-->] -- method

**--------------------- Memento -------------------------**

<Data>_<Boss (Memento)>_<1797883671984>:<__init__>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<print>[<-->] -- method

**[1, 2, 3]**

<Manager>_<client>_<1797883690864>:<remember_data>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<get_state>[<memento getter>] -- method

<DataMemento>_<Memento (Memento)>_<1797883671888>:<__init__>[<-->] -- method

<Manager>_<client>_<1797883690864>:<change_data>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<extend>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<print>[<-->] -- method

**[1, 2, 3, 0, 2, 8, 7, 2]**

<Manager>_<client>_<1797883690864>:<remember_data>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<get_state>[<memento getter>] -- method

<DataMemento>_<Memento (Memento)>_<1797883671408>:<__init__>[<-->] -- method

<Manager>_<client>_<1797883690864>:<change_data>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<extend>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<print>[<-->] -- method

**[1, 2, 3, 0, 2, 8, 7, 2, 3, 9, 8, 2, 0]**

<Manager>_<client>_<1797883690864>:<restore_state>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<restore_state>[<state setter>] -- method

<DataMemento>_<Memento (Memento)>_<1797883671408>:<get_state>[<state getter>] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<print>[<-->] -- method

**[1, 2, 3, 0, 2, 8, 7, 2]**

<Manager>_<client>_<1797883690864>:<restore_state>[<-->] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<restore_state>[<state setter>] -- method

<DataMemento>_<Memento (Memento)>_<1797883671888>:<get_state>[<state getter>] -- method

<Data>_<Boss (Memento)>_<1797883671984>:<print>[<-->] -- method

**[1, 2, 3]**

**--------------------- Observer -------------------------**

<Manager>_<client>_<1797883690864>:<configure_observers>[<-->] -- method

<PredictEventManager>_<Event Manager (observer)>_<1797883672512>:<attach>[<attach observer>] -- method

<PredictEventManager>_<Event Manager (observer)>_<1797883672512>:<attach>[<attach observer>] -- method

<Manager>_<client>_<1797883690864>:<predict_button_pressed>[<-->] -- method

<PredictEventManager>_<Event Manager (observer)>_<1797883672512>:<notify>[<notify observers>] -- method

<Predictor>_<Observer (Observer)>_<1797883672560>:<update>[<do some preparation>] -- method

<Predictor>_<Observer (Observer)>_<1797883672560>:<__get_ready>[<preparation>] -- method

<DataVaultProxy>_<Observer (Observer)>_<1797883672704>:<update>[<do some preparation>] -- method

<DataVaultProxy>_<Observer (Observer)>_<1797883672704>:<__check_connection>[<preparation>] -- method

<DataVaultProxy>_<Observer (Observer)>_<1797883672704>:<__check_something>[<-->] -- method

<Manager>_<client>_<1797883690864>:<reconfigure_observers>[<-->] -- method

<PredictEventManager>_<Event Manager (observer)>_<1797883672512>:<detach>[<detach observer>] -- method

<Manager>_<client>_<1797883690864>:<predict_button_pressed>[<-->] -- method

<PredictEventManager>_<Event Manager (observer)>_<1797883672512>:<notify>[<notify observers>] -- method

<Predictor>_<Observer (Observer)>_<1797883672560>:<update>[<do some preparation>] -- method

<Predictor>_<Observer (Observer)>_<1797883672560>:<__get_ready>[<preparation>] -- method

Process finished with exit code 0
