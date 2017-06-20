from random import randint
from utils import utils
import json
import random


def source_opt_1():
    return utils.select_method_of_input()


def source_opt_2(super_string):
    print("Longitud")
    length = utils.give_me_a_number()
    new_string = ""
    if length < len(super_string):
        top_rand = len(super_string) - length
        irand = randint(0, top_rand)
        new_string = super_string[irand:irand + length]
    else:
        print("length invalido")
    return new_string


def error_base_change(repeat_seq):
    list_repeat_seq = list(repeat_seq)
    len_repeat = len(list_repeat_seq)
    rand = randint(0, len_repeat - 1)
    bases = ['A', 'C', 'T', 'G']
    rand_char = random.choice(bases)
    list_repeat_seq[rand] = rand_char
    return ''.join(list_repeat_seq)


def error_deleted(repeat_seq):
    list_repeat_seq = list(repeat_seq)
    len_repeat = len(list_repeat_seq)
    rand = randint(0, len_repeat - 1)
    list_repeat_seq.pop(rand)
    return ''.join(list_repeat_seq)


def error_insertion(repeat_seq):
    list_repeat_seq = list(repeat_seq)
    len_repeat = len(list_repeat_seq)
    rand = randint(0, len_repeat - 1)
    bases = ['A', 'C', 'T', 'G']
    rand_char = random.choice(bases)
    list_repeat_seq.insert(rand, rand_char)
    return ''.join(list_repeat_seq)


def complement(seq):
    """Return the complementary sequence string."""
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    letters = list(seq)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)


def reverse(seq):
    """Return the sequence string in reverse order."""
    letters = list(seq)
    letters.reverse()
    return ''.join(letters)


def reverse_complement(seq):
    """Return the reverse complement of the dna string."""
    seq = reverse(seq)
    seq = complement(seq)
    return seq


def generate_repeat(dictionary_repeat, super_string):
    list_super_string = list(super_string)

    if dictionary_repeat['times']['a']['selected'] == True:
        times = dictionary_repeat['times']['a']['times']
        # distance
        if dictionary_repeat['distance']['a']['selected'] == True:
            index = dictionary_repeat['distance']['a']['fst_pos']
            distance = dictionary_repeat['distance']['a']['distance']
        else:
            index = 0
            average = dictionary_repeat['distance']['b']['average']
            distance = int(random.expovariate(1 / average))

        if dictionary_repeat['errors']['base_change']['selected'] == True:
            index_base_change = dictionary_repeat['errors']['base_change']['average_distance']
        else:
            index_base_change = -1

        if dictionary_repeat['errors']['deleted']['selected'] == True:
            index_deleted = dictionary_repeat['errors']['deleted']['average_distance']
        else:
            index_deleted = -1

        if dictionary_repeat['errors']['insertion']['selected'] == True:
            index_insertion = dictionary_repeat['errors']['insertion']['average_distance']
        else:
            index_insertion = -1

        if dictionary_repeat['reverse_orientation']['probability'] != 0:
            index_reverse = dictionary_repeat['reverse_orientation']['probability']
        else:
            index_reverse = -1

        for i in range(times):
            if index <= len(list_super_string):
                list_super_string.insert(index, dictionary_repeat['source'])
                index += (len(dictionary_repeat['source']) - 1)
            if dictionary_repeat['distance']['b']['selected'] == True:
                average = dictionary_repeat['distance']['b']['average']
                distance = int(random.expovariate(1 / average))

            if index == index_base_change:
                new_source = error_base_change(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_base_change = dictionary_repeat['errors']['base_change']['average_distance']
                index_base_change += distance_base_change
            if index == index_deleted:
                new_source = error_deleted(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_deleted = dictionary_repeat['errors']['deleted']['average_distance']
                index_deleted += distance_deleted
            if index == index_insertion:
                new_source = error_insertion(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_insertion = dictionary_repeat['errors']['insertion']['average_distance']
                index_insertion += distance_insertion
            if index == index_reverse:
                new_source = reverse_complement(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_reverse = dictionary_repeat['reverse_orientation']['probability']
                index_reverse += distance_reverse

            index = index + distance - 1
    if dictionary_repeat['times']['b']['selected'] == True:
        # distance
        if dictionary_repeat['distance']['a']['selected'] == True:
            index = dictionary_repeat['distance']['a']['fst_pos']
            distance = dictionary_repeat['distance']['a']['distance']
        else:
            index = 0
            average = dictionary_repeat['distance']['b']['average']
            distance = int(random.expovariate(1 / average))

        if dictionary_repeat['errors']['base_change']['selected'] == True:
            index_base_change = dictionary_repeat['errors']['base_change']['average_distance']
        else:
            index_base_change = -1

        if dictionary_repeat['errors']['deleted']['selected'] == True:
            index_deleted = dictionary_repeat['errors']['deleted']['average_distance']
        else:
            index_deleted = -1

        if dictionary_repeat['errors']['insertion']['selected'] == True:
            index_insertion = dictionary_repeat['errors']['insertion']['average_distance']
        else:
            index_insertion = -1

        if dictionary_repeat['reverse_orientation']['probability'] != 0:
            index_reverse = dictionary_repeat['reverse_orientation']['probability']
        else:
            index_reverse = -1

        while(index <= len(list_super_string)):
            if dictionary_repeat['source'] == "":
                new_source = error_insertion(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
            list_super_string.insert(index, dictionary_repeat['source'])
            index += (len(dictionary_repeat['source']) - 1)

            if dictionary_repeat['distance']['b']['selected'] == True:
                average = dictionary_repeat['distance']['b']['average']
                distance = int(random.expovariate(1 / average))

            if index == index_base_change:
                new_source = error_base_change(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_base_change = dictionary_repeat['errors']['base_change']['average_distance']
                index_base_change += distance_base_change
            if index == index_deleted:
                new_source = error_deleted(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_deleted = dictionary_repeat['errors']['deleted']['average_distance']
                index_deleted += distance_deleted
            if index == index_insertion:
                new_source = error_insertion(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_insertion = dictionary_repeat['errors']['insertion']['average_distance']
                index_insertion += distance_insertion

            if index == index_reverse:
                new_source = reverse_complement(dictionary_repeat['source'])
                dictionary_repeat['source'] = new_source
                # update
                distance_reverse = dictionary_repeat['reverse_orientation']['probability']
                index_reverse += distance_reverse

            index = index + distance - 1
    return ''.join(list_super_string)


def base_menu_repeat(super_string):
    dictionary_repeat = {
        "source": "",
        "times": {
            "a": {
                "selected": False,
                "times": 0
            },
            "b": {
                "selected": False
            }
        },
        "distance": {
            "a": {
                "selected": False,
                "fst_pos": 0,
                "distance": 0
            },
            "b": {
                "selected": False,
                "average": 0
            }
        },
        "errors": {
            "base_change": {
                "selected": False,
                "average_distance": 0
            },
            "deleted": {
                "selected": False,
                "average_distance": 0
            },
            "insertion": {
                "selected": False,
                "average_distance": 0
            }
        },
        "reverse_orientation": {
            "probability": 0
        }
    }
    ans = True
    while ans:
        print("""
        +--------+
        | REPEAT |
        +--------+
        1a.Ingresado por el usuario
        1b.Selección aleatoria
        2a.Las veces que quiera
        2b.Las veces que se pueda
        3a.Distancia fija
        3b.Distancia aleatoria
        4a.Errores
        5a.Orientación Inversa
        6a.Generar repeat
        7a.Guardar archivo de configuración
        7b.Cargar archivo de configuración
        9.Regresar
        """)
        ans = input("Ingrese la opción: ")
        if ans == "1a":
            src_string = source_opt_1()
            dictionary_repeat['source'] = src_string
        elif ans == "1b":
            src_string = source_opt_2(super_string)
            dictionary_repeat['source'] = src_string
        elif ans == "2a":
            times = utils.give_me_a_number()
            dictionary_repeat['times']['b']['selected'] = False
            dictionary_repeat['times']['a']['selected'] = True
            dictionary_repeat['times']['a']['times'] = times
        elif ans == "2b":
            dictionary_repeat['times']['a']['selected'] = False
            dictionary_repeat['times']['b']['selected'] = True
            print("Selecionado")
        elif ans == "3a":
            print("Posición inicial")
            fst_pos = utils.give_me_a_number()
            print("Distancia")
            distance = utils.give_me_a_number()
            dictionary_repeat['distance']['b']['selected'] = False
            dictionary_repeat['distance']['a']['selected'] = True
            dictionary_repeat['distance']['a']['fst_pos'] = fst_pos
            dictionary_repeat['distance']['a']['distance'] = distance
        elif ans == "3b":
            print("Distancia Promedio")
            average_distance = utils.give_me_a_number()
            dictionary_repeat['distance']['a']['selected'] = False
            dictionary_repeat['distance']['b']['selected'] = True
            dictionary_repeat['distance']['b']['average'] = average_distance
        elif ans == "4a":
            print("Desea cambio de base (s/n):")
            choice = input(" >>  ")
            choice = choice.lower()
            if choice == "s":
                print("Promedio para cambio de base")
                average = utils.give_me_a_number()
                average_distance = int(random.expovariate(1 / average))
                dictionary_repeat['errors']['base_change']['selected'] = True
                dictionary_repeat['errors']['base_change']['average_distance'] = average_distance

            print("Desea borrado (s/n):")
            choice = input(" >>  ")
            choice = choice.lower()
            if choice == "s":
                print("Promedio para borrado")
                average = utils.give_me_a_number()
                average_distance = int(random.expovariate(1 / average))
                dictionary_repeat['errors']['deleted']['selected'] = True
                dictionary_repeat['errors']['deleted']['average_distance'] = average_distance

            print("Desea inserción (s/n):")
            choice = input(" >>  ")
            choice = choice.lower()
            if choice == "s":
                print("Promedio para inserción")
                average = utils.give_me_a_number()
                average_distance = int(random.expovariate(1 / average))
                dictionary_repeat['errors']['insertion']['selected'] = True
                dictionary_repeat['errors']['insertion']['average_distance'] = average_distance
        elif ans == "5a":
            average = utils.give_me_a_number()
            probability = 0
            if average != 0:
                probability = int(random.expovariate(1 / average))
            dictionary_repeat['reverse_orientation']['probability'] = probability
        elif ans == "6a":
            generated_string = generate_repeat(dictionary_repeat, super_string)
            print(generated_string)
            with open("repeat.txt", "w") as text_file:
                text_file.write(generated_string)
        elif ans == "7a":
            with open('repeat.json', 'w') as json_file:
                json.dump(dictionary_repeat, json_file,
                          indent=4, sort_keys=True)
        elif ans == "7b":
            with open("repeat.json") as json_file:
                dictionary_repeat = json.load(json_file)
                print(dictionary_repeat)
        elif ans == "9":
            return
        elif ans == "99":
            print(json.dumps(dictionary_repeat, indent=4, sort_keys=True))
        elif ans != "":
            print("\n Opción Inválida. Intente de nuevo.")
    return
