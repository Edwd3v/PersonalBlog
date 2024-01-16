import pandas as pd
import random

document_to_tranform = input('Ingresa la ruta del documento: ') 
# Carga el archivo de Excel
df = pd.read_excel(document_to_tranform)

# Guarda el DataFrame en un archivo CSV
number_document = random.randint(1, 100)
df.to_csv(f'data{number_document}.csv', index=False)

