class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def print_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


byd_car = Car('byd', 's7', 2016)

print(byd_car.get_descriptive_name())
byd_car.print_odometer()
