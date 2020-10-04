cars = ['audi', 'benz', 'bmw', 'byd']
print([car.title() for car in cars])

for car in cars:
    if (car == 'bmw' or car == 'byd'):
        print(car.upper())
    else:
        print(car.title())

if 'bmw' in cars:
    print('BMW is in the cars!')
elif 'benz' in cars:
    print('benz is in the cars!')
else:
    print('BMW or Benz is not in the cars!')

available_toppings = [
    'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
    'extra cheese'
]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")