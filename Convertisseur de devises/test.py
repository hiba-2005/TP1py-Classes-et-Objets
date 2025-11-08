from convertisseur import Convertisseur

montant = 100
print("Avant mise a jour :", Convertisseur.vers_dh(montant))

Convertisseur.mettre_a_jour_taux(11.2)
print("Apres mise a jour  :", Convertisseur.vers_dh(montant))