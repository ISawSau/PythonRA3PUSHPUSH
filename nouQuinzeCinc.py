# el exercici agafa una llista de paraules i retorna la suma total de les seves longituds
def total_length(llista):
    suma = 0
    for paraula in llista:
        suma += len(paraula)
    return suma