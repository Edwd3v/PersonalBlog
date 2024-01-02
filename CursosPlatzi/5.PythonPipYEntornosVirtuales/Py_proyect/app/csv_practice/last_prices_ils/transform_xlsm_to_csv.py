import pandas as pd

# Carga el archivo de Excel
df = pd.read_excel('data_prices.xlsm')

# Guarda el DataFrame en un archivo CSV
df.to_csv('data.csv', index=False)

