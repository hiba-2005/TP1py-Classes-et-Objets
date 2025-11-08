from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        timestamp = datetime.now().isoformat()
        self.fichier.write(f"{timestamp} - {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        self.fichier.close()

    @classmethod
    def lire(cls):
        with open("journal.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
        for ligne in reversed(lignes):
            print(ligne.strip())
