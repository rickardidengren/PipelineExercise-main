from dataclasses import dataclass, field
from typing import List


@dataclass
class ChristmasPresent:
    Name: str
    Price: float


@dataclass
class Person:
    Name: str
    Presenter: List[ChristmasPresent] = field(default_factory=list)
    
    def AddPresent(self, present: ChristmasPresent):
        self.Presenter.append(present)
    
    def GetTotal(self) -> float:
        summa = 0
        for x in self.Presenter:
            summa += x.Price
        return summa
