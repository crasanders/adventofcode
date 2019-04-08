with open('polymer.txt', 'r') as file:
    polymer = file.read()


def react(poly):
    for i in range(len(poly)-1):
        cur = poly[i]
        nex = poly[i+1]
        if (cur.isupper() and nex.islower()) or (cur.islower() and nex.isupper()):
            if cur.lower() == nex.lower():
                reacted = poly[:i]
                if i+1 < len(poly):
                    reacted += poly[i+2:]
                return reacted
    return len(poly)


def getlength(poly):
    while type(poly) == str:
        poly = react(poly)

    return poly

print(getlength('aA'))
print(getlength('abBA'))
print(getlength('abAB'))
print(getlength('aabAAB'))
print(getlength('dabAcCaCBAcCcaDA'))

print(getlength(polymer.strip()))