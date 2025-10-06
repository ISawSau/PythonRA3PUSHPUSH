# el programa comprova si dues paraules són anagrames, és a dir, si tenen les mateixes lletres en un ordre diferent
def es_anagrama(paraula1, paraula2):
    """Comprova si dues paraules són anagrames."""

    return sorted(paraula1) == sorted(paraula2)

# el programa carrega una llista de paraules des d’un fitxer
def carrega_paraules(nomDeFitxer):
    """Carrega les paraules d’un fitxer i les retorna com a llista."""
    llista = []
    with open(nomDeFitxer) as fitxer:
        for linia in fitxer:
            paraula = linia.strip()
            llista.append(paraula)
    return llista

# el programa busca tots els anagrames d’una paraula dins d’una llista
def troba_anagrames(objectiu, llista):
    """Troba tots els anagrames de la paraula donada."""
    anagrames = []
    for paraula in llista:
        if paraula != objectiu and es_anagrama(paraula, objectiu):
            anagrames.append(paraula)
    return anagrames

# programa principal
if __name__ == "__main__":
    # carrega les paraules del fitxer 'paraules.txt'
    paraules = carrega_paraules('paraules.txt')

    # defineix la paraula objectiu
    paraula_objectiu = 'canta'

    # troba i mostra els anagrames
    resultat = troba_anagrames(paraula_objectiu, paraules)
    print(f"Anagrames de '{paraula_objectiu}': {resultat}")