
# Sets o Conjuntos en Python

def run():
    
    # Definamos un conjunto de paises para el ejempolo.
    list_latam_countries = ['Colombia', 'Peru', 'Brasil', 'Bolivia', 'Ecuador', 'Argentina', 'Uruguay', 'Colombia', 'Brasil']
    latam_countries = {'Colombia', 'Peru', 'Brasil', 'Bolivia', 'Ecuador', 'Argentina', 'Uruguay', 'Colombia', 'Brasil'}
    print(latam_countries)
    print(list_latam_countries)
    print(type(latam_countries)) # => Class <'sets'>
    print(type(list_latam_countries)) # => Class <'sets'>
    print(len(latam_countries))
    print(len(list_latam_countries))
    # La diferencia con los diccionaros es que los conjuntos no tiene Keys ni Values. Es por eso que podemos diferencia r un diccionario de un conjunto 





if __name__ == '__main__':
    run() 