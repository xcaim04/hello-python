# Variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 45;
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)

# Argumentos de print()

print(my_string_variable, my_int_variable, my_bool_variable)

print(type(my_int_to_str_variable))

print("Hola \n", "Mundo")

# Concatenacion de cadenas
word_one = 'Hi'
word_two = 'Carlos'

print('Este es el valor de: ', my_bool_variable)
print(word_one + word_two)

# NoneType
print(type(print(word_one + word_two)))

# ALgunas funciones del sistema
print(len('Carlos'))

# Variables en una sola linea

"""
Cuidado con abusar de esta sintaxis
Puede traer consigo problemas a la hora de mantenimiento
"""
a, b, c = 5, 10, 15
print(a, b, c)

# Inputs

name = input('What\'s your name? ')
age = input('How old are you? ')

print(name, age)

# Aqui machacas el valor (Tambien puede ser el tipo) que ya tenia name
name = 123

print(name)

"""
Conclusiones: Python es un lenguaje sin tipado fuerte
Tiene un manejo mas eficiente de la memoria, pues
por cada redeclaracion no crea nuevos espacios en la
memoria para el nuevo dato, sino que reutiliza el espacio
ya existente, pero esto puede traer problemas de seguridad
y mantenimiento a largo plazo.
"""

# Forzamos el tipo?
address: str = "C. Andalacia 55"
address = 32
print(type(address))

"""
variable: type = ...
Esta sintaxis NOO da tipado fuerte
solo indica la preferencia de tipo
"""