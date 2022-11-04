import pandas as pd
import matplotlib.pyplot as plt

def cargarArchivo():
    df = pd.read_csv('time_series_covid19_confirmed_ready.csv', header=0)

    return df

df = cargarArchivo()
print(df)

print("-----------------------------------------------------------------")

def ChangeIndex(df):
    return df.set_index('fechas')

df = ChangeIndex(df)
print(df)

print("-----------------------------------------------------------------")

