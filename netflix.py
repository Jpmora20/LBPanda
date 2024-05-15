import pandas as pd
#Importar archivo CSV

file = pd.read_csv("titanic.csv")

# file.info()
#obtener numero especifico de filas al inicio del dataset HEAD(NUMERO DE FILAS)
#file.head()

print(file.head(50))