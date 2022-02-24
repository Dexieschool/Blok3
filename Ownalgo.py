import random
import itertools

# global variables changeable
kleuren=['A','B','C','D','E','F']
lengte=4

perms=itertools.product(kleuren,repeat=lengte)
possible=[p for p in perms]
print(possible)

# global variables
mogelijk = possible.copy()
permslist = []

realcode = random.choices(kleuren,k=lengte)
print("dit is de code:{}" .format(realcode))

#verwijdert steeds de eerste item in de lijst
def permover():
    mogelijk.pop(0)



def simple(code):
    guess = ''.join(mogelijk[0])
    print(guess, 'first guess')
    codecheck = ''.join(code)
    # blijf gokken tot dat het goed is
    count = 1
    while guess != codecheck:
            permover()
            guess = ''.join(mogelijk[0])
            print(guess)
            count += 1
            print('aantal guesses',count)

    return 'je hebt gewonnen'

print(simple(realcode))

