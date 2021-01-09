class Car:
    def __init__(self, model, year, is_self_driving):
        self.model = model
        self.year = year
        self.is_self_driving = is_self_driving


class MustangMach(Car):
    def __init__(self,model, year, is_self_driving):
        super().__init__(model, year, is_self_driving)
        self.model = model
        self.year = year
        self.is_self_driving = is_self_driving

class TeslaModel3(Car):
    def __init__(self,model, year, is_self_driving):
        super().__init__(model, year, is_self_driving)
        self.model = model
        self.year = year
        self.is_self_driving = is_self_driving



c1 = MustangMach("Mustang",2021,False)
c2 = TeslaModel3("TeslaModel3", 2021, True)
print(c1.is_self_driving)
