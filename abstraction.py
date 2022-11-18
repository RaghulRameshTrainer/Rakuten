from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    def get_price(self,model):
        if model=='Figo':
            return 900000
        elif model=='EcoSport':
            return 1600000
        elif model=='Aspire':
            return 1100000
        else:
            return "Please check at showroom"

class NewCar(Car):
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def breaks(self):
        self.breaks_applied=True

    def engine(self):
        self.engine_type='Fuel'

    def seats(self):
        self.seat_capacity='11 Seater'

    def mirror(self):
        self.mirror_condition='Fitted'


c1=NewCar('Ford','EcoSport')
print(c1.get_price('Aspire'))