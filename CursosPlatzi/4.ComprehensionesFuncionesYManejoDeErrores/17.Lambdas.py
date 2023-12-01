def run():

    '''
    def increment(x):
        return x+1
    result = increment(10)
    print(result)

    increment_v2 = lambda x : x + 1
    result = increment_v2(20)    
    print(result)
    '''

    # Ejercicios: Funciones lambda
    # 1. Multiplicación por un valor constante: Crea una función lambda que tome un número como argumento y lo multiplique por un valor constante que defines previamente. Luego, prueba la función con diferentes números.

    Multiplicación_por_un_valor_constante = lambda a: a * 6
    result = Multiplicación_por_un_valor_constante(3)
    print(result)

    # 2. Ordenar lista de tuplas: Dada una lista de tuplas en formato (nombre, edad), utiliza una función lambda para ordenar la lista en función de la edad de las personas

    personas = [
    ("Ana", 25),
    ("Carlos", 32),
    ("Elena", 19),
    ("David", 40),
    ("Luisa", 28)
    ]

    # Ordenar la lista de tuplas por edad utilizando una función lambda
    personas_ordenadas = sorted(personas, key = lambda x: x[1])

    # Imprimir la lista ordenada
    for persona in personas_ordenadas:
        print(persona)    # Imprimir la lista ordenada
    for persona in personas_ordenadas:
        print(persona)
    
    # 3. Filtrar números pares: Crea una función lambda que tome una lista de números como argumento y devuelva una nueva lista solo con los números pares.

    numeros = [3, 8, 12, 7, 6, 19, 25, 10, 14, 21]

    numeros_pares = list(filter(lambda x: x% 2 == 0, numeros))
    print(numeros_pares)








if __name__ == '__main__':
    run()
