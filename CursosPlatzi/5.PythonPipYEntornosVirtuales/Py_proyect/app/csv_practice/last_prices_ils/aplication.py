from datetime import datetime
import read_csv_module
import csv

# Transformar el prin del texto en un CSV
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def write_csv(data, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ["concepto", "referencia", "fecha", "precio"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Tu lista de datos
def run():
    data = read_csv_module.read_csv('./0.documentos_need/data.csv')

    # Estructurar datos
    id_proveedor = []

    for dato in data:
        try:
            fecha = datetime.strptime(dato['FECHA'], '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
        except ValueError:
            fecha = dato['FECHA']  # Si el formato no coincide, simplemente usa la cadena original

        id_proveedor.append({
            "concepto": dato['CONCEPTO'],
            "referencia": dato['REFERENCIA'],
            "fecha": fecha,
            "precio": float(dato['PRECIO UNITARIO'])
        })

    # Crear un diccionario para realizar un seguimiento de la referencia más reciente
    referencias_mas_recientes = {}

    for proveedor in id_proveedor:
        referencia = proveedor['referencia']
        fecha_proveedor = datetime.strptime(proveedor['fecha'], '%Y/%m/%d')

        if referencia in referencias_mas_recientes:
            fecha_existente = datetime.strptime(referencias_mas_recientes[referencia]['fecha'], '%Y/%m/%d')
            if fecha_proveedor > fecha_existente:
                referencias_mas_recientes[referencia] = proveedor
        else:
            referencias_mas_recientes[referencia] = proveedor

    output_path = './resultados.csv'
    write_csv(list(referencias_mas_recientes.values()), output_path)

    print(f'Data written to {output_path}')

if __name__ == '__main__':
    run()