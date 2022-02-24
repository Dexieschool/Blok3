import random
import itertools
from Feedback import feedback

# global variables changeable
kleuren=['A','B','C','D','E','F']
lengte=4

perms=itertools.product(kleuren,repeat=lengte)
possible=[p for p in perms]
print(len(possible))

# global variables
mogelijk = possible.copy()
permslist = []

realcode = random.choices(kleuren,k=lengte)
print("dit is de code:{}" .format(realcode))

def permover(guess,feedbacc):
    permslist = []
    count = 0
    # maakt lijst met alle feedback
    for i in mogelijk:
        permslist.append(feedback(guess, i,lengte))

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
        #maakt een dictionary met elke feedback die wordt teruggegeven
        for a in mogelijk:
            fed = feedback(i, a, lengte)
            fednorm = (list(map(str, fed))) # reformating
            fednorm = ''.join(fednorm)
            if fednorm in templist:
                templist[fednorm] = templist.get(fednorm) + 1
                continue
            elif fednorm not in templist:
                templist[fednorm] = 1
        listdict.append(templist)
        print(templist)
    highest = []
    highestnumber = []

    # zoekt voor worst case van elke dictionary
    for i in listdict:
        highest.append(max(i, key=i.get))
    count = 0
    for i in listdict:
        highestnumber.append(i[highest[count]])
        count += 1
    # pakt de minst erge worst case
    indexmin = min(range(len(highestnumber)), key=highestnumber.__getitem__)
    return indexmin

def simple(code):
    guess = mogelijk[mogelijkheden()]
    codecheck = ''.join(code)
    # blijf gokken tot dat het goed is
    count = 1
    while guess != codecheck:
            feed = feedback(realcode,guess,lengte)
            permover(guess,feed)
            guess = ''.join(mogelijk[mogelijkheden()])
            print(guess)
            count += 1
            print('aantal guesses',count)

    return 'je hebt gewonnen'

print(simple(realcode))

