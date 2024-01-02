import utilies
import read_csv
import charts

def run():
    data = read_csv.read_csv('./data_countries.csv')
    country = input('Type Country => ')
    country = country.capitalize()

    result = utilies.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utilies.get_population(country)
        print(labels, values)
        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()