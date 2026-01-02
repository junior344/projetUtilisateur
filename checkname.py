def checkname(name):
    """
    Vérifie si le nom/prénom contient uniquement des lettres et traits d'union
    """
    if not name:
        return False
    
    for char in name:
        if not (char.isalpha() or char == '-'):
            return False
    return True

def check_nom_prenom_different(nom, prenom):
    """
    Vérifie que le nom et le prénom ne sont pas identiques
    """
    return nom.lower() != prenom.lower()