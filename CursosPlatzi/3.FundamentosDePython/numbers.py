def run ():
     
    budget_jan = int(input('¿Cual es tu presupuesto en el mes de Enero?: '))
    budget_feb = int(input('¿Cual es tu presupuesto en el mes de Febrero?: '))
    budget_mar = int(input('¿Cual es tu presupuesto en el mes de Marzo?: '))

    budget_quartely = budget_jan + budget_feb + budget_mar
    print('Tu presupuesto para los tres meses es de {}'.format(budget_quartely))

    budget_average = budget_quartely / 3
    print("El promedio de ingresos durante los tres meses es de:{}".format(budget_average))

    # OPERADORES LOGICOS
       
if __name__ == '__main__':
    run()


