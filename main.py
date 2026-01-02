# Import des modules de validation
from checkname import checkname, check_nom_prenom_different
from codepostale import code_postal_valide
from checkemail import check_email
from checklogin import check_login, check_login_unique
from module_mots_de_passe import mots_de_passe

def saisir_utilisateur(numero):
    """
    Saisit les informations d'un utilisateur
    """
    print(f"\n=== ENCODAGE UTILISATEUR {numero} ===")
    
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    code_postal = input("Code postal : ")
    email = input("Email : ")
    login = input("Login : ")
    mdp = input("Mot de passe : ")
    
    return nom, prenom, code_postal, email, login, mdp

def valider_utilisateur(nom, prenom, code_postal, email, login, mdp):
    """
    Valide toutes les données d'un utilisateur et retourne les erreurs
    """
    erreurs = []
    
    # Validation nom
    if not checkname(nom):
        erreurs.append("Nom : doit contenir uniquement des lettres et traits d'union")
    
    # Validation prénom
    if not checkname(prenom):
        erreurs.append("Prénom : doit contenir uniquement des lettres et traits d'union")
    
    # Validation nom ≠ prénom
    if nom and prenom and not check_nom_prenom_different(nom, prenom):
        erreurs.append("Nom et prénom : ne peuvent pas être identiques")
    
    # Validation code postal
    if not code_postal_valide(code_postal):
        erreurs.append("Code postal : doit être un code postal belge valide (1000-9992)")
    
    # Validation email
    if not check_email(email):
        erreurs.append("Email : format incorrect (xxx@xxx.xx, seuls . et - autorisés)")
    
    # Validation login
    if not check_login(login):
        erreurs.append("Login : doit être en minuscules uniquement (lettres et chiffres)")
    
    # Validation mot de passe
    if not mots_de_passe(mdp):
        erreurs.append("Mot de passe : minimum 10 caractères avec 1 MAJ, 1 min, 1 chiffre, 1 spécial")
    
    return erreurs

def afficher_rapport(utilisateur_num, erreurs):
    """
    Affiche le rapport de validation
    """
    print(f"\n=== RAPPORT UTILISATEUR {utilisateur_num} ===")
    if erreurs:
        print("❌ ERREURS DÉTECTÉES :")
        for erreur in erreurs:
            print(f"  - {erreur}")
        return False
    else:
        print("✅ TOUTES LES VALIDATIONS SONT OK")
        return True

def afficher_utilisateur_final(nom, prenom, code_postal, email, login, mdp):
    """
    Affiche les informations finales de l'utilisateur avec mot de passe masqué
    """
    mdp_masque = '*' * len(mdp)
    
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")
    print(f"Code postal : {code_postal}")
    print(f"Email : {email}")
    print(f"Login : {login}")
    print(f"Mot de passe : {mdp_masque}")

def main():
    """
    Programme principal
    """
    print("=== SYSTÈME D'ENCODAGE UTILISATEURS ===")
    
    # Variables pour stocker les données des utilisateurs
    utilisateur1_valide = False
    utilisateur2_valide = False
    login1 = ""
    
    # Saisie et validation utilisateur 1
    while not utilisateur1_valide:
        nom1, prenom1, cp1, email1, login1, mdp1 = saisir_utilisateur(1)
        erreurs1 = valider_utilisateur(nom1, prenom1, cp1, email1, login1, mdp1)
        utilisateur1_valide = afficher_rapport(1, erreurs1)
        
        if not utilisateur1_valide:
            print("\n⚠️  Veuillez corriger les erreurs et recommencer.")
        else:
            # Affichage immédiat dès que la validation est OK
            print("\n=== INFORMATIONS UTILISATEUR 1 VALIDÉES ===")
            afficher_utilisateur_final(nom1, prenom1, cp1, email1, login1, mdp1)
    
    # Demander directement si l'utilisateur veut encoder un deuxième utilisateur
    while True:
        reponse = input("\nSouhaitez-vous encoder un deuxième utilisateur ? (o/n) : ").lower().strip()
        if reponse in ['o', 'oui', 'y', 'yes']:
            encoder_deuxieme = True
            break
        elif reponse in ['n', 'non', 'no']:
            encoder_deuxieme = False
            break
        else:
            print("Veuillez répondre par 'o' (oui) ou 'n' (non)")
    
    if encoder_deuxieme:
        # Saisie et validation utilisateur 2
        while not utilisateur2_valide:
            nom2, prenom2, cp2, email2, login2, mdp2 = saisir_utilisateur(2)
            erreurs2 = valider_utilisateur(nom2, prenom2, cp2, email2, login2, mdp2)
            
            # Vérification login unique
            if not check_login_unique(login1, login2):
                erreurs2.append("Login : doit être différent de l'utilisateur 1")
            
            utilisateur2_valide = afficher_rapport(2, erreurs2)
            
            if not utilisateur2_valide:
                print("\n⚠️  Veuillez corriger les erreurs et recommencer.")
            else:
                # Affichage immédiat dès que la validation est OK
                print("\n=== INFORMATIONS UTILISATEUR 2 VALIDÉES ===")
                afficher_utilisateur_final(nom2, prenom2, cp2, email2, login2, mdp2)
    
    # Affichage final récapitulatif
    print("\n" + "="*50)
    print("🎉 ENCODAGE TERMINÉ AVEC SUCCÈS !")
    print("="*50)
    
    print("\n=== RÉCAPITULATIF UTILISATEUR 1 ===")
    afficher_utilisateur_final(nom1, prenom1, cp1, email1, login1, mdp1)
    
    if encoder_deuxieme:
        print("\n=== RÉCAPITULATIF UTILISATEUR 2 ===")
        afficher_utilisateur_final(nom2, prenom2, cp2, email2, login2, mdp2)
    else:
        print("\nAucun deuxième utilisateur encodé.")

if __name__ == "__main__":
    main()
