def run ():
    
    first_word="Hola"
    second_word=" Mundo"
    frase = first_word + second_word

    print(frase)

    def addition (a, b):
        x = a + b
        print(x)

    def substraction (a, b):
        x = a - b
        print(x)

    def multiplication (a, b):
        x = a * b
        print(x)

    def division (a, b):
        x = a // b
        print(x)

    addition (5, 4)
    substraction(30, 4)
    multiplication(20,4)
    division(100, 5)

    my_name = input("¿Cual es tu nombre?: ")
    my_age = input ("¿Cual es tu edad?: ")

    print ("Su nombre es " + str(my_name) + " y su edad es de ", str(my_age), " años.")
    

if __name__ == "__main__":
    run()