# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

def is_a_anagrama(word_one, word_two) -> bool:
    # Words should never be the same
    if word_one == word_two:
        return False
    # The words must always be the same length.
    if len(word_one) != len(word_two):
        return False

    list_letters = list(word_one).sort()
    list_letters_two = list(word_two).sort()

    return list_letters == list_letters_two


if __name__ == '__main__':
    print(is_a_anagrama('amor', 'roma'))
    print(is_a_anagrama('amor', 'romas'))

