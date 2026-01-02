def check_login(login):
    """
    Vérifie si le login est uniquement en minuscules sans caractères spéciaux
    """
    if not login:
        return False
    
    for char in login:
        if not (char.islower() or char.isdigit()):
            return False
    
    return True

def check_login_unique(login1, login2):
    """
    Vérifie que les deux logins ne sont pas identiques
    """
    return login1 != login2
