# el exercici agafa una paraula i mira si conté totes les lletres requerides, si les conté retorna True, si no False
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True
print(uses_all("hola", "hl"))
print(uses_all("hola", "aeiou"))
print(uses_all("programa", "ram"))
print(uses_all("python", "tyn"))
print(uses_all("test", "xyz"))