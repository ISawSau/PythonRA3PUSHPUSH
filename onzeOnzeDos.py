# l'exercici crea una tupla amb dues llistes, afegeix un valor a la segona llista i mostra que no es pot fer servir com a clau d'un diccionari

list0 = [1, 2, 3]
list1 = [4, 5]
t = (list0, list1)

t[1].append(6)

print(t)

try:
    d = {t: 'això és una tupla amb dues llistes'}
except TypeError as e:
    print("Error:", e)