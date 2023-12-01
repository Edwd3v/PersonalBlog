# La funcion filter en python nos permite crear listas a traves de condiciones, en este caso la funcion phyton me ayudara a crear una nueva lista de numeros pares. 

def run():
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list_numbers = list(filter(lambda num: num % 2 == 0, numbers))
    print(new_list_numbers)

if __name__ == '__main__':
    run()