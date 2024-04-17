#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0  # Initialisation de la variable result
    for i in range(1, 3):  # Range de 1 à 2
        try:
            if i > a:  # Vérifie si i est plus grand que a
                raise ValueError('Too far')
            else:
                result += (a ** b) / i
        except ValueError:
            result = a + b
            break
    return result  # Retourne la valeur de result à la fin de la boucle et du code
