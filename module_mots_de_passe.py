'''Module Mots De Passe'''


def mots_de_passe(mdp: str) -> bool:
    '''
    Retourne si le mots de passe respecte les conditions ou pas.
    
        Parametres:
                mdp (str): chaine de caractère contenant (minimum 10 caractères avec minimum 1 MAJ, 1min, 
                1 chiffre et 1 caractère spécial)
        Returns:
                True or False (bool): retourne si le mots de passe et correct ou pas
    '''

    CARACTERE_SPECIAUX = "@#&\"'(§)!-_<>,;:/=+ù%^¨`£$*¥€"

    minuscule = False
    majuscule = False
    chiffre = False
    caract_special = False

    if len(mdp) < 10:
        return False
    
    for c in mdp:

        if c.islower():#vérifier si le caractère est une lettre minuscule
            minuscule = True
            
        elif c.isupper():#vérifier si le caractère est une lettre majuscule
            majuscule = True
            
        elif c in CARACTERE_SPECIAUX:#vérifier si le caratère se trouve dans la variable caractere_speciaux
            caract_special = True

        elif c.isdigit():#vérifier si le caractère est un chiffre
            chiffre = True


    if majuscule and minuscule and caract_special and chiffre:
        return True
    else:
        return False
            
            