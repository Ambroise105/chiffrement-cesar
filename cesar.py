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



clair = input("Quel est votre message : ")
cle = int(input("Quel est la clé de chiffrement : "))


print(chiffrement(clair, cle))