def check_email(email):
    """
    Vérifie si l'email respecte le format xxx@xxx.xx
    Accepte uniquement les lettres, chiffres, points et tirets
    """
    if not email or '@' not in email:
        return False
    
    # Séparer la partie avant et après @
    parties = email.split('@')
    if len(parties) != 2:
        return False
    
    partie_avant, partie_apres = parties
    
    # Vérifier que les parties ne sont pas vides
    if not partie_avant or not partie_apres:
        return False
    
    # Vérifier que la partie après @ contient un point
    if '.' not in partie_apres:
        return False
    
    # Vérifier les caractères autorisés
    caracteres_autorises = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    
    for char in email:
        if char not in caracteres_autorises and char != '@':
            return False
    
    return True
