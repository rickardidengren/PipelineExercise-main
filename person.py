from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    Birthdate:datetime
    Namn:str = ""
    GatuAddress:str= ""
    PostNummer:int= ""
    Postort:str= ""


    def Namnge(self, namn):
        if len(namn) > 1:
            self.Namn = namn
            return True
        return False
        
    def FlyttaInHos(self, another):
        self.GatuAddress = another.GatuAddress
        self.PostNummer = another.PostNummer
        self.Postort = another.Postort
