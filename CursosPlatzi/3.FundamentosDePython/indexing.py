def run():
    
    text = 'PalabraUno'
    # PRIMERA LETRA DE NUESTRO STIRNG
    print(text[0]) # => 'P'

    # ULTIMA LETRA DE NUESTRO STRING
    print (text[-1]) # => 'o'

    # REBANANDO EN STRING
    print(text[0:7]) # => 'Palabra'
    print(text[7:10]) # => 'Uno'
    print(text[:7]) # => 'Palabra'
    print(text[7:]) # => 'Uno'
    
    # SALTOS
    print(text[0:7:2]) # => 'Plba'
    print(text[7:10:2]) # => 'Uo'
    print(text[:7:2]) # => 'Plba'
    print(text[7::2]) # => 'Uo'

if __name__ == '__main__':
    run()