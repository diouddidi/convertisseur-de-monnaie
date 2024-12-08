def convertisseur_de_devise():
    print("Bienvenue dans le convertisseur de monnaie de didi")
    print("choisissez de montant à convertir")
    print("1. EUR -> USD")
    print("2. USD -> EUR")
    print("3. EUR -> CFA")
    print("4. CFA -> EUR")
choix = int (input("Entrer votre choix (1-4): "))
montant= float(input("Entrer le montant à converir: "))

taux_eur_to_usd = 1.10
taux_usd_to_eur = 0.91
taux_eur_to_cfa = 655.96
taux_cfa_to_eur = 1 / 655.96

if choix == 1:
        resultat = montant * taux_eur_to_usd
        print(f"{montant} EUR = {resultat:.2f} USD")
elif choix == 2:
        resultat = montant * taux_usd_to_eur
        print(f"{montant} USD = {resultat:.2f} EUR")
elif choix == 3:
        resultat = montant * taux_eur_to_cfa
        print(f"{montant} EUR = {resultat:.2f} CFA")
elif choix == 4:
        resultat = montant * taux_cfa_to_eur
        print(f"{montant} CFA = {resultat:.2f} EUR")
else:
        print("Choix invalide. Veuillez réessayer.")

convertisseur_de_devise()