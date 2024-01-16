import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
    
if __name__ == '__main__':
    data = read_csv('/home/edwd3v/4.Programing/0.GIT/proyectLapSamsung/CursosPlatzi/5.PythonPipYEntornosVirtuales/Py_proyect/app/csv_practice/last_prices_ils/0.documentos_need/data.csv')
    print(data)