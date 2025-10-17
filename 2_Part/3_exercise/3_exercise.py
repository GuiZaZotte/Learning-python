def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel/12
    return round(salaire_mensuel, 2)

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel/4
    return round(salaire_hebdomadaire, 2)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire/heures_travaillees
    return round(salaire_horaire, 2)

resultat_annuel = float(input("Rentrer votre salaire annuel :\n"))

resultat_heures_travaillees = float(input("Rentrer votre nombre d'heures travaillées :\n"))

resultat_mensuel = salaire_mensuel(resultat_annuel)
print(resultat_mensuel)

resultat_hebdomadaire = salaire_hebdomadaire(resultat_mensuel)
print(resultat_hebdomadaire)

resultat_horaire = salaire_horaire(resultat_hebdomadaire,resultat_heures_travaillees)
print(f"Votre salaire horaire est de {resultat_horaire} euros.")