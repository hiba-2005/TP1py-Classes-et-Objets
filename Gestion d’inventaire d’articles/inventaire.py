
from article import Article

a1 = Article("A001", "Clavier mecanique",  58, 25)
a2 = Article("A002", "Souris sans fil", 30.50, 40)
a3 = Article("A003", "ecran 24 pouces", 175.00, 10)

articles = [a1, a2, a3]

for a in articles:
    print(a)


total = sum(a.valeur_stock() for a in articles)
print(f"\nValeur d_inventaire : {total:.2f} €")


a1.approvisionner(5)
print(f"\nNouveau stock de {a1.designation} : {a1.stock} unites")
