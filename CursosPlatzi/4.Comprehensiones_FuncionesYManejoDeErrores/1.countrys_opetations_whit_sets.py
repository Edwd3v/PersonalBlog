
def run():

    # Creamos un conjuntos de paises
    latam_countries = {'Colombia', 'Argentina', 'Bolivia', 'Brasil', 'Uruguay', 'Paraguay', 'Ecuador', 'Peru', 'Chile', 'Venezuela', 'Panama'}

    nort_america_countries = {'Estados Unidos', 'Canada'}

    central_america_countries = {'Mexico', 'Guatemala', 'El Salvador', 'Cuba', 'Nicaragua'}

    american_countries = {'Estados Unidos', 'Canada','Colombia', 'Argentina', 'Bolivia', 'Brasil', 'Uruguay', 'Paraguay', 'Ecuador', 'Peru', 'Chile', 'Venezuela', 'Panama', 'Mexico', 'El Salvador', 'Guatemala', 'Cuba', 'Nicaragua'} 

    # ¿Cuantos elementos ahi en cada conjunto?
    elements_in_sets = len(latam_countries)
    print('Cantidad de paises en latinoamerica: ', elements_in_sets)
    elements_in_sets_america = len(american_countries)
    print('Cantidad de paises en el continente americano: ', elements_in_sets_america)
    elemenst_in_set_central = len(central_america_countries)
    print('Cantidad de paises en centro america: ', elemenst_in_set_central)
    elements_in_nort = len(nort_america_countries)
    print('Cantidad de paises en el norteamerica: ', elements_in_nort)

    # ¿Como saber si un elementos esta dentro de un conjunto?: Aqui vemos si cierto elemento se enciuentra dentro de un conjuto, es algo asi como un buscador.
    print('Colombia' in latam_countries)
    print('Colombia' in nort_america_countries)
    print('El Salvador' in central_america_countries)

    # ¿Como añadir elementos a un conjunto?
    print('Guayana' in american_countries)
    american_countries.add ('Guayana') 
    print('Guayana' in american_countries)  

if __name__ == '__main__':
    run()