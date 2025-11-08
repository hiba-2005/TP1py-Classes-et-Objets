

class CompteurPage:
   
    total_visites = 0

    def __init__(self, url: str):
   
        self.url = url
        self.visites_par_page = 0  
        
        CompteurPage.total_visites += 1

    def afficher_stats(self) -> str:
        """Retourne les statistiques globales et locales de la page"""
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}, visites page : {self.visites_par_page}"

    def enregistrer_lecture(self):
        """Incrémente le nombre de visites pour cette page spécifique"""
        self.visites_par_page += 1
