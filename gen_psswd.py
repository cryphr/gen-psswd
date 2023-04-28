import random
import string
from colorama import init, Fore, Style

init()

# Pedir al usuario la longitud de la contraseña, si quiere utilizar números y símbolos
length = int(input("Longitud de la contraseña: "))
use_numbers = input("¿Utilizar números? (s/n): ").lower() == "s"
use_symbols = input("¿Utilizar símbolos? (s/n): ").lower() == "s"

# Definir los caracteres a utilizar en la contraseña
characters = string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# Generar la contraseña
password = ''.join(random.choice(characters) for i in range(length))

# Imprimir la contraseña generada en verde
print(Fore.GREEN + "Contraseña generada: " + password + Style.RESET_ALL)
