import os


def give_me_a_float():
    while True:
        try:
            return float(input("Ingrese un número: "))
        except:
            print("Vuelva a intentar...")
            pass


def give_me_a_number():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except:
            print("Vuelva a intentar...")
            pass

# =========
# Metodos para Ingresar secuencias
# =========


def method_file(obj):
    file_path = obj
    with open(file_path) as myfile:
        data = "".join(line.rstrip() for line in myfile)
    return data


def select_method_of_input():
    sequence = ""
    print("Ingrese la secuencia o el path del archivo:")
    obj = input(" >>  ")
    if os.path.exists(obj):
        sequence = method_file(obj)
    else:
        # upper sequence and split to get first
        sequence = ''.join(obj.upper().split())
    return sequence
