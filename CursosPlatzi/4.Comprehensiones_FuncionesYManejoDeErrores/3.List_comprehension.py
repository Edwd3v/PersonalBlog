def run():

    
    # MANERA CONVENCIONAL DE CREAR UNA LISTA (MUCHAS LINEAS DE CODIGO)
    numbers = []
    for element in range(1, 11):
        numbers.append(element)
    print(numbers) # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # FORMA DE CREAR UNA LISTA CON LIST COMPREHESION
    numbers_V2 = [i for i in range(1, 11)]
    print(numbers_V2) # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    numbers_V2 = [i*3 for i in range(1, 11)]
    print(numbers_V2) # => [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    numbers_V3 = [i for i in range (1, 10) if i % 2 == 0]
    print(numbers_V3) # => [2, 4, 6, 8]

if __name__ == '__main__':
    run()