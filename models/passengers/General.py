from models.passengers.Passenger import Passenger

class GeneralPassenger(Passenger):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
    
    def get_discount(self) -> float:
        return 0.0