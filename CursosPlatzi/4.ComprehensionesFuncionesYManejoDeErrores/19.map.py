def run():
    '''
    Esta es la manera mas larga para realizar un ejercicio append
    '''
    numbers = [1, 2, 3, 4]
    numbers_v2 = []
    for i in numbers:
         numbers_v2.append(i * 2)
    print(numbers_v2)

    '''
    Ahora veamos como es la manera corta
     1. Recordemos que la funcion map nos permite hacer transformaciones rapidas de una lista.
     2. En este caso estamos solicitando que haga la treansformación de una lista y para ello estamos utilizando una función lambda.
     3. Recordemos que las funciones tipo lambda nos permiten declarar funciones de manera mas rapida sin nececidad de utilizar def y hacer nuestro codigo mas largo.
     4. Si no transformamos la funcion 'map' en una lista  nos mostrara el mensaje <map object at 0x7f665c2fdf70> que es la representación del objeto map en Python. Indica que has creado un objeto de tipo map mediante la función map() y estás viendo su dirección de memoria en hexadecimal.
     5. La funcion lambda uniocamente nos aydara para hacer funciones simples, que no requieran mas de una linea de codigo y que la funcion no sea tan compleja.    
    '''
    numbers_v3 = list(map(lambda i:i**2, numbers))
    print(numbers_v3)

    '''
    Ahora, intentemos hacer algo mas interesante, supongamos que tenemos dos listas en con 'x' cantidad de elementos y queremos sumar los elementos con su posición correspondiente. es decir la posición [0] de list_1 se suma con la posición [0] de la list_2 
    ''' 
    list_1 = [20, 6, 9, 41, 2]
    list_2 = [11, 18, 56, 3]

    result_sum_lists = list(map(lambda element_list_1, element_list_2: element_list_1 + element_list_2, list_1, list_2 ))
    print(result_sum_lists) # => [31, 24, 65, 44] 
    '''
    Los elementos dentro de nuestra función lambda podemos nombrarlos como queramos pueden ser variables 'x' y 'y' o nombres mas elaborados para saber que es exactamente lo que intentamos hacer y entender nuestro codigo.

    La suma en este caso se limita a la cantidad de elementos de la lista mas pequeña, es decir, si estoy tratando de hacer la operacion con una lista de tres elementos y con otra lista que unicamente contiene dos elementos, mi lista resultante tendra unicamente dos elementos
    '''

    # Ejemplo
    frutas = ["manzana", "banana", "uva", "sandía", "naranja"]
    frutas_deliciosas = list(map(lambda nombre: "deliciosa " + nombre, frutas))
    print(frutas_deliciosas)

if __name__ == '__main__':
    run()
