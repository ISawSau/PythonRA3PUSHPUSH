# el exercici comprova si una paraula és un palíndrom, és a dir, si es llegeix igual d’endavant que d’endarrere
def es_palindrom(paraula):
    return paraula == ''.join(reversed(paraula))

# el programa carrega una llista de paraules des d’un fitxer
def carrega_paraules(nomDeFitxer):
    llista = []
    with open(nomDeFitxer) as fitxer:
        for linia in fitxer:
            paraula = linia.strip()
            llista.append(paraula)
    return llista

# programa principal
if __name__ == "__main__":
    # carrega les paraules del fitxer 'paraules.txt'
    paraules = carrega_paraules('paraules.txt')

    # mostra les paraules que són palíndroms i tenen com a minim 7 lletres
    for paraula in paraules:
        if len(paraula) >= 7 and es_palindrom(paraula):
            print(paraula)