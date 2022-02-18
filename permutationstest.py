import random
import itertools
import time

#kleuren en lengte van de code
kleuren=['A','B','C','D']
lengte=2

#alle combinaties
perms=itertools.product(kleuren,repeat=lengte)
totaal_mogelijkheden=[p for p in perms]
lengte=(len(totaal_mogelijkheden)-1)
print(totaal_mogelijkheden)

mogelijk = totaal_mogelijkheden.copy()
permslist = []


randomnummer = (random.randint(0 , lengte))

# geheime_code = totaal_mogelijkheden[randomnummer]
#
# print('dit is de geheime code' ,geheime_code)

realcode = ['B','C']
print(realcode)


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

    return (helemaal_goed, juiste_kleur)

def permover(guess,feedbacc):
    permslist = []
    count = 0
    for i in mogelijk:
        permslist.append(feedback(guess, i))

    mogelijk2 = mogelijk.copy()

    for a in permslist:
        if a != feedbacc:
            remover = mogelijk2[count]
            mogelijk.remove(remover)

        count += 1
        print(mogelijk)




    print(mogelijk)
    print(permslist)
    return mogelijk[0]


def simple(code):
    guess = 'AA'
    codecheck = ''.join(code)
    while guess != codecheck:

        if guess == codecheck:
            print('je wint')
        if guess != codecheck:
            feed = feedback(realcode,guess)
            guess = ''.join(permover(guess,feed))
            print(guess)
            time.sleep(1)

    return True

simple(realcode)


