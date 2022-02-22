import random
import itertools
import time

# dit is een work in progress

# colors
kleuren=['A','B','C','D']
lengte=2

perms=itertools.product(kleuren,repeat=lengte)
possible=[p for p in perms]

# global variables
mogelijk = possible.copy()
permslist = []

realcode = ['B','C','D','A']
print("dit is de code:{}" .format(realcode))

# feedback functie overgenomen van Lina
def feedback(code, guess):
    # Zet de gok om naar een lijst
    guess = list(guess)

    # De code om de gok mee te vergelijken
    kopie_code = list(code)

    # Juiste kleur op de juiste positie
    helemaal_goed = 0

    # Juiste kleur op de verkeerde positie
    juiste_kleur = 0

    # Loop over de code om de juiste kleur verkeerde positie te bepalen
    for i in range(2):

        # Exacte match?
        if (kopie_code[i] == guess[i]):
            # Een match qua kleur en positie
            helemaal_goed += 1

            # Vervang het stukje code, zodat we deze niet
            # als juiste kleur verkeerde positie kunnen markeren
            kopie_code[i] = '-'
            guess[i] = ''

    # Nu we alle juiste eruit gefilterd hebben kunnen we kijken
    # naar wat nog op de verkeerde plek staat.
    for i in range(2):

        # Zit de kleur ergens anders in de code
        if guess[i] in kopie_code:
            # Verhoog de counter
            juiste_kleur += 1

            # Vervang het element, zodat we geen dubbele feedback krijgen
            kopie_code[kopie_code.index(guess[i])] = '-'
            guess[i] = ''

    return [helemaal_goed, juiste_kleur]


def mogelijkheden():
    listdict = []
    for i in mogelijk:
        templist = {}
        print(listdict,'listdict')
        for a in mogelijk:
            print(a)
            fed = feedback(i, a)
            fednorm = (list(map(str, fed))) # reformating
            fednorm = ''.join(fednorm)
            print(fednorm)
            if fednorm in templist:
                templist[fednorm] = templist.get(fednorm) +1
                continue
            elif fednorm not in templist:
                templist[fednorm] = 1
        listdict.append(templist)
    highest = []

    for i in listdict:
        highest.append(max(i, key=i.get))
    print(highest)

print(mogelijkheden())