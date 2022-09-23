def chiffrement(texte, offset):
    """Fonction pour chiffrer le message de l'utilisateur
    param1: texte(str) - Texte à chiffrer
    param2: offset(int) - Clé de chiffrement utilisé
    return: message_chiffre(str) - Message chiffré
    """

    message_chiffre = ""
    valeur = ""

    for i in texte:

        valeur = ord(i)+offset

        if valeur > 122:
            message_chiffre += chr((valeur)-26)

        else:
            message_chiffre += chr(valeur)

    return message_chiffre


def dechiffrement(texte, offset):
    """Fonction pour déchiffrer le message de l'utilisateur
    param1: texte(str) - Texte à déchiffrer
    param2: offset(int) - Clé de déchiffrement utilisé
    return: message_dechiffre(str) - Message déchiffré
    """

    message_dechiffre = ""
    valeur = ""

    for i in texte:
        
        valeur = ord(i)-offset

        if valeur < 97:
            message_dechiffre += chr((valeur)+26)

        else:
            message_dechiffre += chr(valeur)

    return message_dechiffre



clair = input("Quel est votre message : ")
cle_chiffrement = int(input("Quel est la clé de chiffrement : "))


print(chiffrement(clair, cle_chiffrement))


chiffre = input("Quel est votre message chiffré : ")
cle_dechiffrement = int(input("Quel est la clé de déchiffrement : "))

print(dechiffrement(chiffre, cle_dechiffrement))