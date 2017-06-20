import os
import sys
import math
import numpy as np

from utils import utils


def unequal_bases(random_size):
    while True:
        print("Probalidad de A")
        a_prob = utils.give_me_a_float()
        print("Probalidad de C")
        c_prob = utils.give_me_a_float()
        print("Probalidad de T")
        t_prob = utils.give_me_a_float()
        print("Probalidad de G")
        g_prob = utils.give_me_a_float()

        list_of_probabilities = [a_prob, c_prob, t_prob, g_prob]

        total = math.fsum(list_of_probabilities)
        if total != 1.0:
            print("Las probabilidades debe sumar 1.0")
        else:
            break
    aa_milne_arr = ['A', 'C', 'T', 'G']
    ran = np.random.choice(aa_milne_arr, random_size, p=list_of_probabilities)

    return ''.join(ran)


def completely_random(random_size):
    aa_milne_arr = ['A', 'C', 'T', 'G']
    ran = np.random.choice(aa_milne_arr, random_size,
                           p=[0.25, 0.25, 0.25, 0.25])

    return ''.join(ran)


def base_menu():
    ans = True
    while ans:
        print("""
        1.Ingresada por el usuario
        2.Totalmente aleatoria
        3.Bases desiguales
        4.Cancelar
        """)
        ans = input("Ingrese la opción: ")
        if ans == "1":
            return utils.select_method_of_input()
        elif ans == "2":
            print("Tamaño")
            random_size = utils.give_me_a_number()
            return completely_random(random_size)
        elif ans == "3":
            print("Tamaño")
            random_size = utils.give_me_a_number()
            return unequal_bases(random_size)
        elif ans == "4":
            return ""
        elif ans != "":
            print("\n Opción Inválida. Intente de nuevo.")
    return ""


# Main Program
if __name__ == "__main__":
    # Launch main menu
    base_menu()
