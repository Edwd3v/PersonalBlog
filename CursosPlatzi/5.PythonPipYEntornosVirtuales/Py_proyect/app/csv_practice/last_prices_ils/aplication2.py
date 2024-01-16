from datetime import datetime
import csv
import pandas as pd
import random
import tkinter as tk
from tkinter import filedialog

def read_csv_module(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def read_csv():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    # Abre el cuadro de diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls"), ("Excel files", "*.xlsx")])

    if not file_path:
        print("No se seleccionó ningún archivo.")
        return None

    return file_path

def write_csv(data, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ["concepto", "referencia", "fecha", "precio"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

def transform_excel_to_csv():
    document_to_transform = read_csv()
    if document_to_transform:
        # Carga el archivo de Excel
        df = pd.read_excel(document_to_transform)

        # Guarda el DataFrame en un archivo CSV
        number_document = random.randint(1, 100)
        output_path = f'data{number_document}.csv'
        df.to_csv(output_path, index=False)

        print(f'Documento transformado y guardado como {output_path}')
        return output_path
    else:
        return None

def run():
    csv_path = transform_excel_to_csv()

    if csv_path:
        data = read_csv_module(csv_path)

        # Estructurar datos
        id_proveedor = []

        for dato in data:
            fecha_str = dato.get('Fecha')

            if fecha_str is not None and fecha_str != '':
                try:
                    fecha = datetime.strptime(fecha_str, '%Y/%m/%d').strftime('%Y-%m-%d')
                except ValueError:
                    fecha = None
            else:
                fecha = None

            id_proveedor.append({
                "concepto": dato.get('Texto Captura Concepto'),
                "referencia": dato.get('Referencia'),
                "fecha": fecha,
                "precio": float(dato.get('Vr. Unitario', 0))  # Usamos 0 como valor por defecto si no hay 'Vr. Unitario'
            })

        # Imprimir el progreso para depuración
        print("Datos estructurados. Procesando referencias...")

        # Crear un diccionario para realizar un seguimiento de la referencia más reciente
        referencias_mas_recientes = {}

        for proveedor in id_proveedor:
            referencia = proveedor.get('referencia')
            fecha_proveedor = datetime.strptime(proveedor.get('fecha', ''), '%Y-%m-%d') if proveedor.get('fecha') else None

            if referencia is not None:
                if referencia in referencias_mas_recientes:
                    fecha_existente = datetime.strptime(referencias_mas_recientes[referencia].get('fecha', ''), '%Y-%m-%d') if referencias_mas_recientes[referencia].get('fecha') else None
                    if fecha_proveedor and (not fecha_existente or fecha_proveedor > fecha_existente):
                        referencias_mas_recientes[referencia] = proveedor
                else:
                    referencias_mas_recientes[referencia] = proveedor

        # Imprimir el progreso para depuración
        print("Referencias procesadas. Escribiendo resultados...")

        output_path = './resultados.csv'
        write_csv(list(referencias_mas_recientes.values()), output_path)

        print(f'Data written to {output_path}')

if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(f"Error inesperado: {e}")
