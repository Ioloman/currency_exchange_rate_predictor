import predictor as pd
from super_prediction_module import SuperPredict
from random import randint

if __name__ == '__main__':
    # ------------ Adapter ----------------
    print('------------ Adapter ----------------')
    new_predictor = SuperPredict()
    try:
        new_predictor.predict(pd.DataLeaf(0))
    except AttributeError as e:
        print(e)

    new_predictor = pd.SuperPredictAdapter()
    new_predictor.predict(pd.DataLeaf(0))

    # ----------------- Decorator -----------------
    print('----------------- Decorator -----------------')
    empty = pd.EmptyVisualizer()
    basic = pd.BaseVisualizer()

    empty.show()
    basic.show()

    empty = pd.Visualizer1(empty)
    basic = pd.Visualizer2(basic)

    empty.show()
    basic.show()

    empty = pd.Visualizer2(empty)
    empty.show()

    # -------------- Composite --------------------------
    print('-------------- Composite --------------------------')
    print('---------------- Начало создания -------------------')
    data = pd.DataComposite([
        pd.DataComposite([pd.DataLeaf(randint(0, 100)) for i in range(randint(1, 10))])
        for j in range(randint(1, 10))
    ])
    print('------------------- Начало сохранения ------------------------')
    data.save()
    print('------------------- Начало поиска границ ------------------------')
    print(data.borders())
    print('------------------- Начало поиска среза ------------------------')
    sl = data.slice(50, 101)
    print('------------------- Вывод ------------------------')
    print(sl)

    # -------------- Iterator --------------------------
    print('-------------- Iterator --------------------------')

    result = list(sl)
    print('-------------- Преобразование в строку --------------------------')
    print(' '.join(map(str, result)))



