import csv
from collections import defaultdict
from datetime import datetime

# Tu lista de datos

# Diccionario para realizar un seguimiento de la última fecha y precio de compra para cada referencia
ultimas_compras = defaultdict(lambda: {'FECHA': datetime.min, 'PRECIO UNITARIO': 0.0})

# Procesar los datos para obtener la última fecha y precio de compra para cada referencia
for compra in data:
    try:
        fecha_compra = datetime.strptime(compra['FECHA'], '%Y/%m/%d')  # Intentar el formato esperado
    except ValueError:
        # Si falla, intentar el otro formato
        fecha_compra = datetime.strptime(compra['FECHA'], '%Y-%m-%d %H:%M:%S')
    if fecha_compra > ultimas_compras[compra['REFERENCIA']]['FECHA']:
        ultimas_compras[compra['REFERENCIA']]['FECHA'] = fecha_compra
        ultimas_compras[compra['REFERENCIA']]['PRECIO UNITARIO'] = float(compra['PRECIO UNITARIO'])

# Resultado: Lista de las últimas compras para cada referencia
ultimas_compras_lista = [{'REFERENCIA': referencia, 'ULTIMA FECHA': info['FECHA'].strftime('%Y/%m/%d'), 'ULTIMO PRECIO UNITARIO': info['PRECIO UNITARIO']} for referencia, info in ultimas_compras.items()]
# Imprimir el resultado
for compra in ultimas_compras_lista:
    pass
    #print(compra)
referencia_especifica = 'BF1212 / HCX8019G/FLP486'  # Coloca aquí la referencia que te interesa
for compra in ultimas_compras_lista:
    if compra['REFERENCIA'] == referencia_especifica:
        print(f"Referencia: {compra['REFERENCIA']}")
        print(f"Fecha de última compra: {compra['ULTIMA FECHA']}")
        print(f"Precio de última compra: {compra['ULTIMO PRECIO UNITARIO']}")
        break  # Termina el bucle una vez que encuentres la referencia específica

else:
    print(f"No se encontró información para la referencia: {referencia_especifica}")

# Resultado: Lista de las últimas compras para cada referencia
ultimas_compras_lista = [
    {
        'REFERENCIA': referencia,
        'ULTIMA FECHA': info['FECHA'].strftime('%Y/%m/%d'),
        'ULTIMO PRECIO UNITARIO': info['PRECIO UNITARIO'],
        'CONCEPTO': data[0]['CONCEPTO']
    }
    for referencia, info in ultimas_compras.items()
]

# Especifica el nombre del archivo CSV
archivo_csv = 'resultados_ultimas_compras.csv'

# Abre el archivo CSV en modo de escritura
with open(archivo_csv, 'w', newline='') as csvfile:
    # Define los encabezados del archivo CSV
    fieldnames = ['REFERENCIA', 'ULTIMA FECHA', 'ULTIMO PRECIO UNITARIO', 'CONCEPTO']

    # Crea el objeto escritor CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribe los encabezados en el archivo CSV
    writer.writeheader()

    # Escribe las filas de datos en el archivo CSV
    for compra in ultimas_compras_lista:
        writer.writerow({
            'REFERENCIA': compra['REFERENCIA'],
            'ULTIMA FECHA': compra['ULTIMA FECHA'],
            'ULTIMO PRECIO UNITARIO': compra['ULTIMO PRECIO UNITARIO'],
            'CONCEPTO': compra['CONCEPTO']
        })

# Imprime un mensaje indicando que la operación se realizó con éxito
print(f"Los resultados se han almacenado en {archivo_csv}")

