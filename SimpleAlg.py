import random
import itertools
import time
from Feedback import feedback


# global variables Changeable
kleuren = ['A','B','C','D','E','F']
lengte=4

perms=itertools.product(kleuren,repeat=lengte)
possible=[p for p in perms]

# Global variables
mogelijk = possible.copy()
permslist = []


realcode = random.choices(kleuren,k=lengte)
print("dit is de code:{}" .format(realcode))


def permover(guess,feedbacc):
    permslist = []
    count = 0
    # maakt lijst met alle feedback
    for i in mogelijk:
        permslist.append(feedback(guess, i, lengte))

    mogelijk2 = mogelijk.copy()
    # checkt welke feedback niet gelijk is aan de feedback die gekregen is van de
    # de echte code te vergelijken met de input
    for a in permslist:
        if a != feedbacc:
            remover = mogelijk2[count]
            mogelijk.remove(remover)

        count += 1


    return mogelijk[0]


def simple(code):
    guess = 'AAAA'
    codecheck = ''.join(code)
    # blijf gokken tot dat het goed is
    while guess != codecheck:
            feed = feedback(realcode,guess,lengte)
            guess = ''.join(permover(guess,feed))
            print(guess)
            time.sleep(1)

    return 'je hebt gewonnen'

print(simple(realcode))


