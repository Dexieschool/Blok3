
a = "abcdefg"
b = "bcdefgh"
c = "abcdejg"

# opdracht 2 string check
def string_check(s1,s2):
    matches = 0
    for i in range(len(s1)):
        if i == len(s2):
            break
        if s1[i] == s2[i]:
            matches += 1
    return matches


#opdracht 1 piramide
def stermaker(hoogte):
    for i in range(hoogte):
        print((i+1) * "*")
    for a in range((hoogte - 1),0,-1):
        print(a * "*")

    return


# reverse piramide
def revermaker(hoogte):
    count1 = 1
    count2 = hoogte -1
    for i in range(hoogte,0,-1):
        print((i -1) * " "+ count1 *"*")
        count1 += 1
    for a in range(1,hoogte):
        print(a * " "+ count2* "*")
        count2 -= 1
    return

lijstcheck = [1,10,3]
# opdracht 3 lijstcheck a
def lijstchecker(list,nummer):
    aantal = 0
    for i in list:
        if i == nummer:
            aantal += 1
    return aantal

#lijst check b
def afstandcheck(lijst):
    count = 1
    newlist = []
    for i in range(len(lijst)):
        if count == len(lijst):
            max1 = max(newlist)
            return max1
        if lijst[i] > lijst[count]:
            newlist.append(lijst[i] - lijst[count])
        if lijst[i] < lijst[count]:
            newlist.append(lijst[count] - lijst[i])
        if lijst[i] == lijst[count]:
            newlist.append(0)
        count += 1


#lijst check c
eennullist = [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
def eenennul(lijst):

    aantal_nul = lijstchecker(lijst,0)
    aantal_een = lijstchecker(lijst,1)

    if aantal_nul > 12:
        return False
    if aantal_een > aantal_nul:
        return True
    else:
        return False



print(eenennul(eennullist))


# opdracht 4

def palingdroom(woord):
    reverse1 = woord[::-1]
    if reverse1 == woord:
        return True
    else:
        return False

def palingdroomzelf(woord):
    reverse = ''

    for i in range(len(woord )-1,-1,-1):
        reverse += woord[i]
    if reverse == woord:
        return True
    else:
        return False

# opdractht 5 sorteren

list1 = [1,90,3,10,3,25]

def sorteren(lst):
    for items in range(len(lst)): # sort list
        for items2 in range(items + 1, len(lst)):
            if lst[items] > lst[items2]:
                lst[items], lst[items2] = lst[items2], lst[items]
    return lst


# opdracht 6 gemiddelde

lijstlijst = [[1,2,3,4],[90,90,30],[23,42,23]]

def gemiddelde(lijst):
    gemiddelde1 = []
    for i in lijst:
        sum = 0
        count = 0
        for a in i:
            count += 1
            sum += a

        gemiddelde1.append(sum/count)

    return gemiddelde1

# print(gemiddelde(lijstlijst))

# opdracht 7 random

def random():
    import random
    n = random.randint(1,10)
    i = int(input("probeer het getal tussen de tien te raden"))
    while i != n:
        if i > n:
            print('je zit te hoog')
            i = int(input())
        if i < n:
            print("je zit te laag")
            i = int(input())
    print("je hebt het geraden")
    return "je hebt het geraden"

# random()


# opdracht 8 compressie

def compressie():
    f = open("compresme", "r")
    new = open("compressed.txt","x")
    temp = ""
    for x in f:
        for a in x:
            if a != "" and a != ' ':
                temp += a
    temp = temp.replace("\n",'')
    new.write(temp)
    new.close()
    f.close()
    return

# compressie()


# opdracht 9 verschuiven
# kom hier niet uit
def verschuiving(woord,verschuif):
    wordlen = len(woord)
    if verschuif < 0:
        change = verschuif % -wordlen
    if verschuif > 0:
        change = verschuif % wordlen
    if change == 0:
        return woord
    else:
        hold = woord[:change] + woord[change:]
        return hold

print(verschuiving('123456',2))

# TODO: abcdefg
# opdracht 10 fibonaci

def fibonaci(n):
    count = 0
    first = 0
    second = 1

    if n == 1:
        return 0

    while count < n -1:
        sum = first + second
        first = second
        second = sum
        count += 1
    return sum

print(fibonaci(100))
# ceasar opdracht 11

def ceasar():
    inp = input("geef een tekst")
    rot = int(input("geef een rotatie"))
    realrot = rot % 26
    alph = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    newtekst = ""
    for i in inp:
        if i == " ":
            newtekst += " "
            continue
        placement = alph.index(i)
        i = alph[placement+realrot]
        newtekst += i
    return newtekst



# #h
# print(ceasar())


#opdracht 12 fizzbuz

def fizzbuzz():
    for i in range(100):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()