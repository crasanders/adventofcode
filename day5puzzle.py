with open('polymer.txt', 'r') as file:
    polymer = file.read().strip()

#puzzle 1
def react(polymer):
    chain = []
    for unit in polymer:
        if len(chain) < 1:
            chain.append(unit)
        else:
            cur = chain[-1]
            if ((cur.isupper() and unit.islower()) or (cur.islower() and unit.isupper())) and cur.lower() == unit.lower():
                chain.pop(-1)
            else:
                chain.append(unit)

    return len(chain)


print(react('aA'))
print(react('abBA'))
print(react('abAB'))
print(react('aabAAB'))
print(react('dabAcCaCBAcCcaDA'))

print(react(polymer))


#puzzle 2
def whichunit(polymer):
    bestunit = ''
    lowest = len(polymer)
    typs = ''.join(set(polymer.lower()))
    for typ in typs:
        reduced_polymer = polymer.replace(typ, '').replace(typ.upper(), '')
        length = react(reduced_polymer)
        if length < lowest:
            bestunit = typ
            lowest = length
    return bestunit, lowest

print(whichunit('dabAcCaCBAcCcaDA'))
print(whichunit(polymer))
