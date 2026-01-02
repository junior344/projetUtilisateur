code_postal_entre = input("Entrer votre code postal : ")

def code_postal_valide(cp):
    # Vérifie si ce sont des chiffres, si la longueur est 4
    # et si le nombre est compris entre 1000 et 9992
    if cp.isdigit() and len(cp) == 4:
        if 1000 <= int(cp) <= 9992:
            return True
    return False

# Utilisation
if code_postal_valide(code_postal_entre):
    print(" Code conforme au format belge.")
else:
    print(" Code invalide.")