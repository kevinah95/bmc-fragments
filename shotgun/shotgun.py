from utils import utils
from random import *
import json


def shotgun(dictionary_fragments, super_string):

    quantity = dictionary_fragments['quantity']
    length = dictionary_fragments['length']
    deviation = dictionary_fragments['deviation']
    coverage = dictionary_fragments['coverage']

    arr_size_fragments = []
    for i in range(quantity):
        arr_size_fragments.append(int(round(uniform(
            length - deviation, length + deviation))))

    fragmentos = []

    if(coverage):
        if(quantity * length < len(super_string)):
            print("Fragmentos insuficientes para cubrir toda la hilera base")
            return fragmentos
        else:
            index = 0
            for i in range(quantity):
                if index > (len(super_string) - min(arr_size_fragments)):
                    index = randint(0, len(super_string) -
                                    min(arr_size_fragments))
                newIndex = index + arr_size_fragments[i]
                fragmentos.append(super_string[index:newIndex])
                index = newIndex
    else:
        for i in range(quantity):
            index = randint(0, len(super_string) - min(arr_size_fragments))
            fragmentos.append(
                super_string[index:(index + arr_size_fragments[i])])
    return fragmentos

# shotgun("ACGTGACGATCGATTAGGCTAGCGAGGCTAGAC",6,6,2,True,True,2,True)


def base_menu_shotgun(super_string):
    dictionary_fragments = {
        "quantity": 0,
        "length": 0,
        "deviation": 0,
        "coverage": 0
    }
    ans = True
    while ans:
        print("""
        +---------+
        | SHOTGUN |
        +---------+
        1a.Ingrese la cantidad
        1b.Tamaño de fragmentos
        1c.Desviación Estándar
        1d.Cobertura
        2a.Generar Fragmentos
        3a.Guardar archivo de configuración
        3b.Cargar archivo de configuración
        9.Regresar
        """)
        ans = input("Ingrese la opción: ")
        if ans == "1a":
            print("Cantidad de fragmentos")
            quantity = utils.give_me_a_number()
            dictionary_fragments['quantity'] = quantity
        elif ans == "1b":
            print("Tamaño de fragmentos")
            length = utils.give_me_a_number()
            dictionary_fragments['length'] = length
        elif ans == "1c":
            print("Deviación")
            deviation = utils.give_me_a_number()
            dictionary_fragments['deviation'] = deviation
        elif ans == "1d":
            yesno = input("Desea cobertura total (s/n)")
            if yesno.lower() == "s":
                dictionary_fragments['coverage'] = True
            else:
                dictionary_fragments['coverage'] = False
        elif ans == "2a":
            fragments = shotgun(dictionary_fragments, super_string)
            print(fragments)
            file = open('fragments.txt', 'w')
            for item in fragments:
                file.write("%s\n" % item)
        elif ans == "3a":
            with open('fragments.json', 'w') as json_file:
                json.dump(dictionary_fragments, json_file,
                          indent=4, sort_keys=True)
        elif ans == "3b":
            with open("fragments.json") as json_file:
                dictionary_fragments = json.load(json_file)
                print(dictionary_fragments)
        elif ans == "9":
            return
        elif ans != "":
            print("\n Opción Inválida. Intente de nuevo.")
    return
