codes_postaux_principaux = [
    1000, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, # Bruxelles
    1300, 1400, 1410, # Brabant Wallon
    2000, 2800, # Anvers / Malines
    3000, 3500, # Louvain / Hasselt
    4000, 4500, 4800, # Liège / Huy / Verviers
    5000, 5500, # Namur / Dinant
    6000, 6700, # Charleroi / Arlon
    7000, 7500, # Mons / Tournai
    8000, 8400, # Bruges / Ostende
    9000, 9100  # Gand / Saint-Nicolas
]
#il ya 1159 codes postaux en belgique
code_postal_entre=input("Entrer votre code postal : ")
longueur=len(code_postal_entre)
#print(code_postal_entre)
def code_postal_valide(code_postal_entre):
    if longueur ==4:

        if int(code_postal_entre[0])>=1:

         if int(code_postal_entre) in codes_postaux_principaux:

          print("Code postal valide")
         else:
          print("Code postal invalide")
        else:
          print("le premier chiffre de votre code postal doit etre entre 1 et 9")
    else:
         print("votre code postal doit contenir 4 chiffres")

code_postal_valide(code_postal_entre)