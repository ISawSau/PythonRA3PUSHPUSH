# el exercici agafa una llista de paraules i retorna la suma total de les seves longituds
def total_length(llista):
    suma = 0
    for paraula in llista:
        suma += len(paraula)
    return suma

print(total_length(["hola", "món"]))
print(total_length(["a", "b", "c"]))
print(total_length(["programació", "python"]))
print(total_length([""]))
print(total_length(["una", "llista", "de", "paraules"]))