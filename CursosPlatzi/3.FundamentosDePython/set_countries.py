


def run():
    
    countries = {"MX", "COL", "ARG", "USA"}
    northAm = {"USA", "CANADA"}
    centralAm = {"MX", "GT", "BZ"}
    southAm = {"COL", "BZ", "ARG"}

    new_set = set()
    # Escribe tu solución 👇
    new_set = (countries | northAm | centralAm | southAm)
    print(new_set)


if __name__ == '__main__':
    run