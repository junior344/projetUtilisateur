# PROJET-UTILISATEUR

## Description
Système d'encodage et de validation d'utilisateurs développé en Python. Ce programme permet de saisir et valider les informations de deux utilisateurs en respectant des critères stricts de validation pour chaque champ.

## Fonctionnalités

### Validation des champs utilisateur
Le programme valide les informations suivantes pour chaque utilisateur :

- **Nom et Prénom** : Uniquement des lettres et traits d'union, doivent être différents
- **Code postal** : Format belge (4 chiffres, entre 1000 et 9992)
- **Adresse email** : Format xxx@xxx.xx avec uniquement lettres, chiffres, points et tirets
- **Login** : Uniquement en minuscules (lettres et chiffres), doit être unique
- **Mot de passe** : Minimum 10 caractères avec au moins 1 majuscule, 1 minuscule, 1 chiffre et 1 caractère spécial

### Fonctionnalités du programme
- Rapport détaillé des erreurs de validation
- Correction interactive des erreurs
- Affichage sécurisé (mot de passe masqué)
- Possibilité d'encoder un deuxième utilisateur (optionnel)
- Vérification d'unicité des logins

## Structure du projet

```
projetUtilisateur/
├── main.py                      # Programme principal
├── checkname.py                 # Validation nom/prénom
├── codepostale.py              # Validation code postal belge
├── checkemail.py               # Validation adresse email
├── checklogin.py               # Validation login
├── module_mots_de_passe.py     # Validation mot de passe
└── README.md                   # Documentation
```

## Installation et exécution

### Prérequis
- Python 3.x installé sur votre système

### Exécution
```bash
cd /home/josias/Documents/esa-cours/programmation/projetUtilisateur
python main.py
```

## Utilisation

### Déroulement du programme
1. **Saisie utilisateur 1** : Le programme demande toutes les informations
2. **Validation** : Rapport d'erreurs si des champs sont invalides
3. **Correction** : Possibilité de corriger les erreurs
4. **Affichage immédiat** : Dès que tout est OK, affichage avec mot de passe masqué
5. **Option deuxième utilisateur** : Possibilité d'encoder un 2e utilisateur
6. **Vérification unicité** : Contrôle que les logins sont différents
7. **Récapitulatif final** : Présentation des utilisateurs validés

### Exemple d'utilisation
```
=== ENCODAGE UTILISATEUR 1 ===
Nom : Dupont
Prénom : Jean-Pierre
Code postal : 1000
Email : jean.dupont@email.be
Login : jdupont
Mot de passe : MonMotDePasse123!

✅ TOUTES LES VALIDATIONS SONT OK

=== INFORMATIONS UTILISATEUR 1 VALIDÉES ===
Nom : Dupont
Prénom : Jean-Pierre
Code postal : 1000
Email : jean.dupont@email.be
Login : jdupont
Mot de passe : ******************
```

## Règles de validation détaillées

### Nom et Prénom
- ✅ Lettres uniquement (a-z, A-Z)
- ✅ Traits d'union autorisés (-)
- ✅ Nom différent du prénom
- ❌ Chiffres interdits
- ❌ Caractères spéciaux interdits (sauf trait d'union)

### Code postal
- ✅ Format belge : 4 chiffres
- ✅ Plage valide : 1000 à 9992
- ❌ Codes invalides : 0000-0999, 9993-9999

### Email
- ✅ Format : xxx@xxx.xx
- ✅ Caractères autorisés : lettres, chiffres, points, tirets
- ✅ Un seul @ obligatoire
- ✅ Au moins un point après @
- ❌ Autres caractères spéciaux interdits

### Login
- ✅ Minuscules uniquement
- ✅ Chiffres autorisés
- ✅ Unicité entre les deux utilisateurs
- ❌ Majuscules interdites
- ❌ Caractères spéciaux interdits

### Mot de passe
- ✅ Minimum 10 caractères
- ✅ Au moins 1 majuscule (A-Z)
- ✅ Au moins 1 minuscule (a-z)
- ✅ Au moins 1 chiffre (0-9)
- ✅ Au moins 1 caractère spécial (@#&"'(§)!-_<>,;:/=+ù%^¨`£$*¥€)

## Architecture du code

### Principe d'étanchéité
Chaque module est responsable d'une validation spécifique :
- Fonctions pures sans effets de bord
- Paramètres d'entrée clairement définis
- Valeurs de retour booléennes ou listes d'erreurs
- Aucune dépendance entre les modules de validation

### Modules de validation

#### checkname.py
- `checkname(name)` : Valide format nom/prénom
- `check_nom_prenom_different(nom, prenom)` : Vérifie différence

#### codepostale.py
- `code_postal_valide(cp)` : Valide code postal belge

#### checkemail.py
- `check_email(email)` : Valide format email

#### checklogin.py
- `check_login(login)` : Valide format login
- `check_login_unique(login1, login2)` : Vérifie unicité

#### module_mots_de_passe.py
- `mots_de_passe(mdp)` : Valide complexité mot de passe

## Exemples de données valides

```python
# Exemples valides
nom = "Dupont-Martin"
prenom = "Jean-Pierre"
code_postal = "1050"
email = "jean.dupont@email.be"
login = "jdupont123"
mot_de_passe = "MonMotDePasse123!"
```

## Gestion des erreurs

Le programme affiche des messages d'erreur explicites :
- 📝 Description précise du problème
- 🔄 Possibilité de correction immédiate
- ✅ Validation en temps réel
- 📊 Rapport complet avant affichage final

## Sécurité

- 🔒 Mot de passe jamais affiché en clair
- 🎭 Masquage par astérisques (*)
- 🔐 Validation robuste des critères de complexité
- 🛡️ Prévention des logins dupliqués

## Auteur

Projet développé dans le cadre du cours de programmation ESA.

---

