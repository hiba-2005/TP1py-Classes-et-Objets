

class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        """Calcule la valeur totale du stock pour cet article."""
        return self.prix_ht * self.stock

    def approvisionner(self, qte: int):
        """Augmente le stock et journalise l_operation."""
        self.stock += qte
        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"Approvisionnement {self.reference} : +{qte} unites (nouveau stock : {self.stock})\n")

    def __str__(self) -> str:
        return f"Ref {self.reference} — {self.designation} : {self.stock} unites a {self.prix_ht:.2f} € HT"
