def describe_pet(animal_type, pet_name):
    print("\n I have a " + animal_type + ", My " + animal_type +
          "'s name is " + pet_name.title() + ".")


describe_pet('dog', 'wangcai')

describe_pet(animal_type='cat', pet_name='erniu')

describe_pet(pet_name='erniu', animal_type='cat')


def get_formatted_name(firstName, lastName, middleName=''):
    if middleName == '':
        fullName = (firstName + ' ' + lastName).title()
    else:
        fullName = (firstName + ' ' + middleName + ' ' + lastName).title()
    return fullName


print(get_formatted_name('lv', 'hui', 'ri'))

print('lv hongfang'.title())


def build_person(first_name, last_name, middle_name=''):
    person = {'fistName': first_name, 'lastName': last_name}
    if middle_name:
        person['middleName'] = middle_name
    return person


print(build_person('lv', 'rihui'))
print(build_person('lv', 'hui', 'ri'))
'''
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' to quit at any time)")
    f_name = input("First name:")
    if f_name.lower() == 'q':
        break
    l_name = input("Last name:")
    if l_name.lower() == 'q':
        break
    full_name = get_formatted_name(f_name, l_name)
    print("\nHello," + full_name + "!")
'''


def greet_users(names):
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
greet_users(usernames[0])