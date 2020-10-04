class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.oil = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def print_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_oil(self, oil):
        self.oil += oil

    def print_oil(self):
        print("This car has " + str(self.oil) + " oil in it.")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def print_batter_size(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_battery_size(self):
        return self.battery_size

    def get_range(self):
        if self.battery_size > 70:
            range = self.battery_size * 3
        elif self.battery_size > 40:
            range = self.battery_size * 2.5
        elif self.battery_size > 20:
            range = self.battery_size * 2
        else:
            range = self.battery_size * 1.5
        return range


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(10)

    def print_battery(self):
        print("This car has a " + str(self.battery.get_battery_size()) +
              "-kWh battery.")

    def fill_oil(self, oil):
        print("This car doesn't need oil")

    def print_oil(self):
        print("This car doesn't need oil")


byd_car = Car('byd', 's7', 2016)
print(byd_car.get_descriptive_name())
byd_car.print_odometer()

my_byd_elec = ElectricCar('byd-elec', '宋Max', 2020)
print(my_byd_elec.get_descriptive_name())
my_byd_elec.print_odometer()
my_byd_elec.print_battery()
my_byd_elec.print_oil()
my_byd_elec.fill_oil(2)
print(my_byd_elec.battery.get_range())