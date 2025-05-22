from dataclasses import dataclass, field

@dataclass
class ChristmasPresent:
    Name:str
    Price:float

@dataclass
class Person:
    Name:str
    Presenter = field(default_factory=list)
    
    def AddPresent(self,present):
        self.Presenter.append(present)
    
    def GetTotal(self):
        summa = 0
        for x in self.Presenter:
            summa = summa + x.Price
        return summa
