import predictor as pd
from datetime import date


if __name__ == '__main__':
    client = pd.Manager()
    # --------------------- Strategy -------------------------
    print('--------------------- Strategy -------------------------')
    print('need second source')
    client.extract_data('rub', date.today(), 'year', source='2')
    print('need first source')
    client.extract_data('rub', date.today(), 'year', source='1')

    # --------------------- Memento -------------------------
    print('--------------------- Memento -------------------------')

    data = pd.Data([1, 2, 3])

    data.print()
    client.remember_data(data)
    client.change_data(data)
    data.print()
    client.remember_data(data)
    client.change_data(data)
    data.print()
    client.restore_state(data)
    data.print()
    client.restore_state(data)
    data.print()

    # --------------------- Observer -------------------------
    print('--------------------- Observer -------------------------')

    client.configure_observers()
    client.predict_button_pressed()

    client.reconfigure_observers()
    client.predict_button_pressed()



