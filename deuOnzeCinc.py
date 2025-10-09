# la funció combina dos diccionaris de comptadors i retorna un nou diccionari amb la suma dels valors

def add_counters(counter1, counter2):
    resultat = dict(counter1)
    for clau, valor in counter2.items():
        resultat[clau] = resultat.get(clau, 0) + valor
    return resultat

def value_counts(paraula):
    comptador = {}
    for lletra in paraula:
        comptador[lletra] = comptador.get(lletra, 0) + 1
    return comptador

counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')

print(counter1)
print(counter2)
print(add_counters(counter1, counter2))