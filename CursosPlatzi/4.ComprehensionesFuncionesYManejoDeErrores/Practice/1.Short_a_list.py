# Ordenar una lista de tuplas por el segundo elemento:
# Dada una lista de tuplas, ordena la lista en función del segundo elemento de cada tupla utilizando una función lambda.

def run ():

    tuplas = [(3, 6), (1, 8), (2, 4), (5, 2)]
    # Ordena la lista de tuplas utilizando una función lambda para comparar el segundo elemento.
    tuplas_ordenadas = sorted(tuplas, key = lambda x: x[1])
    print(tuplas_ordenadas)


if __name__ == '__main__':
    run()