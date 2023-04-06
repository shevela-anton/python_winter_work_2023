# Задание 20-2
import pandas as pd
def summ(dct):
    df = pd.DataFrame(dct)
    return df.sum(numeric_only = True)


dct = {'column1': ['a', 'b', 'c', 'x'], 'column2': [1, 2, 3, 4]}

print(summ(dct))