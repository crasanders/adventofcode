with open('polymer.txt', 'r') as file:
    polymer = file.read()


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

print(react(polymer.strip()))