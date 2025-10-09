# la funció rep un diccionari amb comptadors i retorna una llista de claus amb valors majors que 1

def find_repeats(counter):
    """Makes a list of keys with values greater than 1."""
    resultats = []
    for clau, valor in counter.items():
        if valor > 1:
            resultats.append(clau)
    return resultats

print(find_repeats({'a': 3, 'b': 1, 'c': 2}))
print(find_repeats({'x': 1, 'y': 1, 'z': 1}))
print(find_repeats({'p': 5, 'q': 2, 'r': 1}))