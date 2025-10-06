#el exercici agafa una paraula i mira si esta a una llista, si està a una llista retorna True, si no False
def uses_none(word, available):
    for letter in word:
        if letter not in available:
            return False
        return True
print(uses_none("hola", "aeiouhln"))
print(uses_none("hola", "aeiou"))
print(uses_none("python", "aeiou"))
print(uses_none("aaa", "a"))
print(uses_none("test", "est"))