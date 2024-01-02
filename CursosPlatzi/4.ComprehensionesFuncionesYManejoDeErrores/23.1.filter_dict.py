def run():

    matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Germany',
    'away_team': 'France',
    'home_team_score': 2,
    'away_team_score': 2,
    'home_team_result': 'Draw'
},
{
    'home_team': 'Brazil',
    'away_team': 'Argentina',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
},
{
    'home_team': 'Spain',
    'away_team': 'Italy',
    'home_team_score': 1,
    'away_team_score': 2,
    'home_team_result': 'Loss'
},
{
    'home_team': 'USA',
    'away_team': 'Canada',
    'home_team_score': 0,
    'away_team_score': 2,
    'home_team_result': 'Loss'
},
{
    'home_team': 'Japan',
    'away_team': 'South Korea',
    'home_team_score': 2,
    'away_team_score': 2,
    'home_team_result': 'Draw'
}
]
    
#   print(matches)
#   print (len(matches))

# Con estas lineas de codigo podemos saber cuales de los paises jugaron de locales
#    for matches in matches:
#        print(matches['home_team'])

    
    win_matches = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
    print(win_matches)

    cont = 1
    for game in win_matches:
        print('El {} país ganador es: {}'.format(cont, game['home_team']))
        cont += 1
    '''
    def home_team():
        for match in new_list:
            print(new_list['home_team'])
    return home_team
    '''
if __name__ == '__main__':
    run()