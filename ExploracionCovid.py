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

print(df[['Costa.Rica','Uruguay', 'Brazil', 'Spain', 'Italy', 'France', 'Canada']].loc['1/23/2020':'10/15/2020'])

print("-----------------------------------------------------------------")
df2 = df[['Costa.Rica']]
df2.plot()
plt.show()

df[['Spain', 'Italy', 'France']].loc['1/23/2020':'10/15/2020'].plot()
plt.show()