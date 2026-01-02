def code_postal_valide(cp):
    """
    Vérifie si ce sont des chiffres, si la longueur est 4
    et si le nombre est compris entre 1000 et 9992 (format belge)
    """
    if cp.isdigit() and len(cp) == 4:
        if 1000 <= int(cp) <= 9992:
            return True
    return False