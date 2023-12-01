def run ():
    # Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

    # La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.  

    def multiply_numbers(numbers):
        operation = list(map(lambda number: number * 2, numbers))
        return operation

    numbers = [1, 2, 3, 4]
    response = multiply_numbers(numbers)
    print(response)

    '''
    # Metodo largo
    numbers_2 = []
    for num in numbers:
        multipli_number = num*2
        numbers_2.append(multipli_number)
    print(numbers_2)
    '''
    
if __name__ == '__main__':
    run()