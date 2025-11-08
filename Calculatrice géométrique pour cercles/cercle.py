from math import pi

class Cercle:
    def __init__(self, rayon):
        self._rayon = None
        self.rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, valeur):
        if valeur <= 0:
            raise ValueError("Le rayon doit être positif et non null.")
        self._rayon = valeur

    @property
    def perimetre(self):
        return 2 * pi * self._rayon

    @property
    def surface(self):
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage):
        self.rayon *= (1 + pourcentage / 100)
