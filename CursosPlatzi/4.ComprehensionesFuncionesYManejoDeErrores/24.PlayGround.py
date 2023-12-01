# Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras. La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

def run():
    
    # Esta funcion nos permite filtrar en la listas 'Words' las palabras con 4 letras o más
    def filter_by_length(words):
        filter_of_words = list(filter(lambda word: len(word) >= 4, words))
        return filter_of_words

    words = ['amor', 'sol', 'piedra', 'día']
    response = filter_by_length(words)
    print(response)

if __name__ == '__main__':
    run()