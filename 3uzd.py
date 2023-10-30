"""
Uzrakstiet programmu, izveidot klasi ar nosaukumu
Dati. Izveidot objektu, kas inicializētu atribūtus, 
piemēram, vārdu, vecumu un ceļojumam iemaksāto summu.

"""



class Dati:
    def __init__(self, vards, vecums, celojums):
        self.vards=vards,
        self.vecums=vecums, 
        self.celojums=celojums

dati = Dati("Jānis", 12, 400)
