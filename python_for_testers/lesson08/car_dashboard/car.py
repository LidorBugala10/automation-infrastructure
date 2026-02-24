class Car:
    def __init__(self,fuel_level,km_per_liter):
        self.fuel_level = fuel_level
        self.km_per_liter = km_per_liter
    def drive(self,distance):
        fuel_required = distance / self.km_per_liter
        if self.fuel_level > fuel_required:
            self.fuel_level -= fuel_required
            print("Trip successful")
        else :
            print("not enough fuel for this trip")






