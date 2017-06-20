import sys
from sequence_generator import sequence_generator
from repeat import repeat
from palindrome import palindrome
from shotgun import shotgun

super_string = ""

ans = True
while ans:
    print("""
    +------+
    | MAIN |
    +------+
    1.Hilera Base
    2.Repeat
    3.Palidrome
    4.Shotgun
    5.Salir
    """)
    ans = input("Ingrese la opción: ")
    if ans == "1":
        super_string = sequence_generator.base_menu()
    elif ans == "2":
        if super_string != "":
            repeat.base_menu_repeat(super_string)
        else:
            print("Debe de ingresar la hilera base.")
    elif ans == "3":
        if super_string != "":
            palindrome.base_menu_palindrome(super_string)
        else:
            print("Debe de ingresar la hilera base.")
    elif ans == "4":
        if super_string != "":
            shotgun.base_menu_shotgun(super_string)
        else:
            print("Debe de ingresar la hilera base.")
    elif ans == "5":
        sys.exit()
    elif ans != "":
        print("\n Not Valid Choice Try again")
