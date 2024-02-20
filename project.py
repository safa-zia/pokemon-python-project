import random
import requests
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    print(response)
    pokemon = response.json()
    return {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
    'base experience': pokemon['base_experience'],
    'hp': pokemon['stats'][0]['base_stat'],
    'defend': pokemon['stats'][1]['base_stat'],
    'attack': pokemon['stats'][2]['base_stat']
    }
def game():
 random_pokemon()
print('Your pokemon is {}'.format(random_pokemon()['name']))
who_chooses = input('Will you let the opponent choose which stat to play? me/opponent')
if who_chooses == 'me':
   which_stat = input('What stat would you like to use? (id, height, weight, base experience, hp, defend, attack)')
else:
    number = random.randint(1, 7)
    if number == 1:
        which_stat = 'id'
        print('Your stat is {}'.format(which_stat))
    elif number == 2:
        which_stat = 'height'
        print('Your stat is {}'.format(which_stat))
    elif number == 3:
        which_stat = 'weight'
        print('Your stat is {}'.format(which_stat))
    elif number == 4:
        which_stat = 'base experience'
        print('Your stat is {}'.format(which_stat))
    elif number == 5:
        which_stat = 'hp'
        print('Your stat is {}'.format(which_stat))
    elif number == 6:
        which_stat ='defend'
        print('Your stat is {}'.format(which_stat))
    else:
        which_stat = 'attack'
        print('Your stat is {}'.format(which_stat))

opposing_pokemon = random_pokemon()
print('The opponents pokemon is {}'.format(opposing_pokemon['name']))
player_stat = random_pokemon()[which_stat]
opponent_stat = opposing_pokemon[which_stat]
if player_stat > opponent_stat:
    print('Player wins')
elif player_stat < opponent_stat:
    print('Player lost')
else:
    print('Player drew with opponent')
game()






















