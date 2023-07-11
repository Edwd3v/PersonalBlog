def run():

# EJERCICIO DE PRACTICA DE LA CLASE    

    # Ciclo for normal y corriente como lo hemos venido aplicando.
#    numbers = []

#    for num in  range(1, 11):
#        numbers.append(num)
#    print(numbers)

    # El mismo ciclo for de arriba pero ahora con 'List Comprhension' esto es muy util ya que nos permite ahorrar lineas de codigo inecesaria cuando desehemos realizar un loop o ciclo. 
#    numbers = [number for number in range(1, 11)]
#    print('Lista de numeros entre el 1, 11: ',numbers)

# EJERCICIOS CON CHAT GPT

    # Ejercicio 1:
    #Escribe un programa que tome una lista de números como entrada y genere una nueva lista que contenga el cuadrado de cada número en la lista de entrada.

    ejercicio_1 = [number**2 for number in range (1, 11)]
    print('Ejercicio 1: Elevación al cuadrado: ', ejercicio_1)

    #Ejercicio 2:
    #Escribe un programa que tome una lista de palabras como entrada y genere una nueva lista que contenga la longitud de cada palabra en la lista de entrada.

    #ejercicio_2 = ["gato", "perro", "manzana", "casa", "sol"]
    ejercicio_2 = [len(word) for word in ["gato", "perro", "manzana", "casa", "sol"]]
    print('Ejercicio 2: Cantidad letras: ', ejercicio_2)
    
    #while len(ejercicio_2) < 10:
    #    count = 0
    #    string = input("You word: ")
    #    count = len(string)
    #    long_word.append(count)
    #    ejercicio_2.append(string)
        #print(len(ejercicio_2), ejercicio_2)
    #print(ejercicio_2)
    #print(long_word)

    #def obtener_longitud_palabras(lista_palabras):
    #    return [len(palabra) for palabra in lista_palabras]    
    #obtener_longitud_palabras(['Casa', 'Perro', 'Comer'])
    
    #Ejercicio 3:
    #Escribe un programa que tome una lista de números como entrada y genere una nueva lista que contenga solo los números pares de la lista de entrada.

    ejercicio_3 = [number for number in [26 ,45, 60, 84, 22, 30, 66, 12, 93, 99, 82, 15] if number%2 == 0]
    ejercicio_3_1 = [number for number in [26 ,45, 60, 84, 22, 30, 66, 12, 93, 99, 82, 15] if number%2 != 0]
    print('Ejercicio 3: Números pares: ',ejercicio_3)
    #print('Ejercicio 3.1:', ejercicio_3_1)
    #print(len(ejercicio_3))
    #print(len(ejercicio_3_1))
    #print(len(ejercicio_3)+len(ejercicio_3_1))

    #Ejercicio 4:
    #Escribe un programa que tome una lista de palabras como entrada y genere una nueva lista que contenga solo las palabras que empiecen con la letra 'a' en la lista de entrada.

    ejercicio_4 = [ word for word in ['apple', 'banana', 'cat', 'dog', 'elephant', 'ant', 'frog', 'alligator', 'giraffe', 'aardvark', 'peach', 'kiwi', 'apricot', 'lemon', 'lime', 'avocado', 'grape', 'orange', 'pear', 'watermelon'] if word[0] == 'a']
    print('Ejercicio 4: Palabra con a: ', ejercicio_4)


    #Ejercicio 5:
    #Escribe un programa que tome una lista de números como entrada y genere una nueva lista que contenga solo los números mayores que 10 de la lista de entrada.

    ejercicio_5 = [ bignumber for bignumber in [26 ,45, 60, 84, 22, 30, 66, 12, 93, 99, 82, 15, 2, 7, 56, 4, 1] if bignumber > 10 ]
    print('Ejercicio 5: Mayor a 10: ', ejercicio_5)

    #Ejercicio 6:
    #Escribe un programa que imprima los números del 1 al 10, pero solo aquellos que sean múltiplos de 3.

    ejercicio_6 = [number for number in range (1, 11) if number % 3 == 0 ]
    print('Ejercicio 6: Multiplos de 3: ', ejercicio_6)

    #Ejercicio 7:
    #Escribe un programa que recorra una lista de números y cuente cuántos de ellos son mayores que 100.
    ejercicio_7 = [number for number in [56, 486, 210, 20, 3659, 101, 100, 465] if number > 100]
    print('Ejercicio 7: Mayores a 100: ', ejercicio_7)

    #Ejercicio 8
    #Escribe un programa que itere sobre una lista de palabras e imprima solo aquellas que tengan más de 5 caracteres.
    ejercicio_8 = [ word for word in ['apple', 'banana', 'cat', 'dog', 'ant', 'frog', 'giraffe', 'peach', 'kiwi', 'apricot', 'lemon', 'lime', 'avocado', 'grape', 'orange', 'pear', 'watermelon'] if len(word) > 5 ]
    print('Ejercicio 8: Más de cinco caracteres: ', ejercicio_8)


    #Ejercicio 9
    #Escribe un programa que calcule la suma de todos los números pares del 1 al 50.
    ejercicio_9 = sum([sumnum for sumnum in range(1, 51) if sumnum % 2 == 0 ])
    print('Ejercicio 9: Suma de los pares 1 al 50: ', ejercicio_9)

    #Ejercicio 10
    #Escribe un programa que recorra una lista de números y sume solo aquellos que sean divisibles por 5 o por 7.
    ejercicio_10 =  sum([number for number in [5, 7, 11, 13, 15, 20, 21, 25, 22, 31] if number % 5 == 0 or number % 7 == 0 ])
    print('Ejercicio 10: Suma de numeros divisibles por 5 o 7: ', ejercicio_10)

if __name__ == '__main__':
    run()