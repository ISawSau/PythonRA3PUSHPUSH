# el exercici agafa una frase i inverteix l’ordre de les paraules, posant la primera en majúscula i les altres en minúscula
def reverse_sentence(frase):
    paraules = frase.split()
    paraules_invertides = paraules[::-1]
    resultat = [paraules_invertides[0].capitalize()] + [p.lower() for p in paraules_invertides[1:]]
    return ' '.join(resultat)