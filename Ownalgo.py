import random
import itertools
import time

# dit is een work in progress

# colors
kleuren=['A','B','C','D','E','F']
lengte=4

perms=itertools.product(kleuren,repeat=lengte)
possible=[p for p in perms]
print(len(possible))

# global variables
mogelijk = possible.copy()
permslist = []

realcode = ['A','F','D','F']
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
    for i in range(4):

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
    for i in range(4):

        # Zit de kleur ergens anders in de code
        if guess[i] in kopie_code:
            # Verhoog de counter
            juiste_kleur += 1

            # Vervang het element, zodat we geen dubbele feedback krijgen
            kopie_code[kopie_code.index(guess[i])] = '-'
            guess[i] = ''

    return [helemaal_goed, juiste_kleur]


def permover(guess,feedbacc):
    permslist = []
    count = 0
    # maakt lijst met alle feedback
    for i in mogelijk:
        permslist.append(feedback(guess, i))

    mogelijk2 = mogelijk.copy()
    # checkt welke feedback niet gelijk is aan de feedback die gekregen is van de
    # de echte code te vergelijken met de input
    for a in permslist:
        if a != feedbacc:
            remover = mogelijk2[count]
            mogelijk.remove(remover)

        count += 1

def mogelijkheden():
    listdict = []
    for i in mogelijk:
        templist = {}
        for a in mogelijk:
            fed = feedback(i, a)
            fednorm = (list(map(str, fed))) # reformating
            fednorm = ''.join(fednorm)
            if fednorm in templist:
                templist[fednorm] = templist.get(fednorm) +1
                continue
            elif fednorm not in templist:
                templist[fednorm] = 1
        listdict.append(templist)
    highest = []
    highestnumber = []
    for i in listdict:
        highest.append(max(i, key=i.get))
    count = 0
    for i in listdict:
        highestnumber.append(i[highest[count]])
        count += 1
    indexmin = max(range(len(highestnumber)), key=highestnumber.__getitem__)
    return indexmin

def simple(code):
    guess = ''.join(mogelijk[mogelijkheden()])
    print(guess,'first guess')
    codecheck = ''.join(code)
    # blijf gokken tot dat het goed is
    count = 1
    while guess != codecheck:
            feed = feedback(realcode,guess)
            permover(guess,feed)
            guess = ''.join(mogelijk[mogelijkheden()])
            print(guess)
            count += 1
            print('aantal guesses',count)

    return 'je hebt gewonnen'

print(simple(realcode))

