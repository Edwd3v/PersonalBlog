def run():

    # Creamos una lista de diccionarios, es decir una lista cuyos elementos son diccionarios, cada uno de estos diccionarios son prendas de vestir.
    # Lo que vamos a hacer es crear una lista con la función 'map' y utilizando la sintaxis corta que nos permite realizar la función 'lambda'

    items = [
        {
            'product':'Shirt(Camisa)',
            'price': 100
        },        
        {
            'product':'Pants(Pantalon)',
            'price': 45
        },
        {
            'product':'Socks(Medias)',
            'price': 60
        }
            ]

    # Creamos la lista 'prices' que nos ayudara a filtrar en una los precios de los productos en la lista de diccionarios llamada 'items' 
    prices = list(map(lambda item: item['price'], items))
    # Recordemos que para que nos salga en pantalla lo que contiene la lista al momento del print debemos transformar todo el contenido en una lista.
    # Basicamente lo que estamos haciendo es que 'item' dentro de la funcion representa cada uno de los diccionarios y decimos que la funcion lambda
    # va a tomar el valor de la llave llamada 'price' dentro de cada diccionario.
    print(prices)

if __name__ == '__main__':
    run()

