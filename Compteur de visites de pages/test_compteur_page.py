
from compteur_page import CompteurPage


p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

p1.enregistrer_lecture()
p1.enregistrer_lecture()
p2.enregistrer_lecture()


for p in (p1, p2, p3):
    print(p.afficher_stats())


print(f"\nTotal des visites globales : {CompteurPage.total_visites}")
