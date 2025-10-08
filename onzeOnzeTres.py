# l'exercici defineix una funció que aplica un xifratge César desplaçant les lletres d'una paraula segons un nombre donat
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

def shift_word(paraula, desplacament):
    resultat = []
    for lletra in paraula:
        index_nou = (letter_map[lletra] + desplacament) % len(letters)
        resultat.append(letters[index_nou])
    return ''.join(resultat)

print(shift_word("cheer", 7))
print(shift_word("melon", 16))