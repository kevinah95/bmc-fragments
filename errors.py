repeat = ["A", "T", "G"]
position = int(input("Ingrese la posición de la mutación"))


# Eliminación de bases

def delate(repeat, position):
    repeat.pop(position - 1)
    return(repeat)


print (delate(repeat, position))


# Cambio de base

new_base = input("Ingrese la base con la que desea intercambiar")
# Al correrlo, se debe ingresar la base con comillas para que funcione


def sustitution(repeat, position, new_base):
    repeat[position - 1] = new_base
    return(repeat)


print(sustitution(repeat, position, new_base))
