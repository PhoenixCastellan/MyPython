#topping是一个元组对象，传入的参数会被构建未元组
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping.title())


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza_v2(size, *toppings):
    print("\nMaking a " + str(size) +
          " -inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping.title())


make_pizza_v2(15, 'pepperoni')
make_pizza_v2(16, 'mushrooms', 'green peppers', 'extra cheese')


def make_pizza_v3(size, **toppings):
    print("\nMaking a " + str(size) +
          " -inch pizza with the following toppings:")
    for key, value in toppings.items():
        print("-" + key.title() + "," + value.title())


make_pizza_v3(16, v1='mushrooms', v2='green peppers', v3='extra cheese')


'''
细究def make_pizza_v2(size, *toppings):
    def make_pizza_v3(size, **toppings):
    的差异，前者是给非关键字实参，后者是给关键字实参
'''