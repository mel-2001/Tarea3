import pandas as pd
from numpy import mean, std

datos = {'nombre': ["Juan Carlos","Francisco","Edudardo","Anabelle","Sonia","Mathew","Jimmy"],
         'carrera': ["Ing. Eléctrica","Educacion Física","Matemáticas","Ing. Mecánica","Derecho","Idiiomas","Ing. Civil"],
         'Edad': [21,20,19,29,22,21,22]
         }

df = pd.DataFrame()

df['Nombre'] = datos['nombre']
df['Carrera'] = datos['carrera']
df['Edad'] = datos['Edad']
listaIndices = []
cont = 0
while cont < len(df):
    texto = "est" + str(cont)
    listaIndices.append(texto)
    cont += 1
df['Indices'] = listaIndices
df = df.set_index('Indices')
print(df)
print("----------------------------------------------")

# Ordenar por nombre
print("\n Ordenar por nombre\n")
print(df.sort_values(by=['Nombre']))
print("----------------------------------------------")

# Ordenar por carrera descendente
print("\n Ordenar por carrera descendente\n")
print(df.sort_values(by='Carrera', ascending=False))
print("----------------------------------------------")

#  visualización usando el índice numeral (iloc) 
print("\nVisualización usando el índice numeral (iloc)\n")
print(df.iloc[[0]])
print(df.iloc[[1]])
print(df.iloc[[2]])
print("----------------------------------------------")

#  visualización usando el índice textual de los estudiantes a partir de la tercera entrada.
print("\nVisualización usando el índice textual (iloc)\n")
print(df.loc[["est0"]])
print(df.loc[["est1"]])
print(df.loc[["est2"]])
print("----------------------------------------------")
