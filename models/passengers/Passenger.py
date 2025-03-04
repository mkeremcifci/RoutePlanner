from abc import ABC, abstractmethod

class Passenger(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_discount(self) -> float:
        pass

    def __str__(self):
        return f"Passenger: {self.name}, Age: {self.age}"