
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def run():
    
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(alfabet)
    alfabet_mul_tree = alfabet[::3]
    alfabet_mul_tree.remove('a')
    for letter in alfabet_mul_tree:
        alfabet.remove(letter)        
    print(alfabet)

    # OTRA SOLUCIÒN ES:
    

    alphabet_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
    for i in range(len(alphabet_1), 1, -1): 
    # los parametros del anterior rango nos dicn: el plimer parametro es la cantidad de elementos, el segundo parasmetro determina el inicio del buclo o la posiciòn hasta la cuan se va a iterar y teniendo en cuenta que este ciclo for empieza desde el final debido al parametro -1. Esto se hace con el fin de Si el ciclo for comenzara desde el principio de la lista, y se eliminara un elemento en una posición determinada, entonces los índices de los elementos restantes cambiarían, lo que resultaría en una iteración incorrecta del bucle y se podrían omitir elementos o procesar elementos adicionales. Al recorrer la lista en orden inverso, el bucle evita este problema, ya que siempre se eliminarán los elementos con los índices más altos primero, y los índices de los elementos restantes en la lista no cambiarán. Por lo tanto, se puede eliminar elementos de la lista sin afectar la iteración del bucle y asegurarse de que se eliminen todos los elementos múltiplos de 3 de la lista.
        if i % 3 == 0:
            alphabet_1.pop(i-1)
    print(alphabet_1)

if __name__ == '__main__':
    run()