#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0  # Initialisation de la variable result

    # Boucle for
    for i in range(1, 3):  # Range de 1 à 2
        try:
            if i > a:  # Vérifie si i est plus grand que a
                raise Exception('Too far')  # Lance une exception si i est trop grand
        except Exception:
            result += (a ** b) / i  # Calcule (a**b)/i et ajoute le résultat à result
        else:
            result += a + b  # Si aucune exception n'est levée, ajoute a+b à result
        finally:
            pass  # Ne fait rien dans le bloc finally

    return result  # Retourne la valeur de result à la fin de la boucle et du code
