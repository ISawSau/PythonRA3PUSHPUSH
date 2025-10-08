# la funció retorna Treu si hi ha un caràcter que apareix més d'un cop a la seqüència

def has_duplicates(paraula):
    for lletra in paraula:
        if paraula.count(lletra) > 1:
            return True
    return False

print(has_duplicates("unpredictably"))
print(has_duplicates("java"))
print(has_duplicates("oriol"))
print(has_duplicates("wey"))