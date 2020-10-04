aliens = [{'color': 'green', 'age': 5, 'position': {'x': 0, 'y': 25}}]

print(aliens[0])
print(aliens[0]['color'])

aliens[0]['sex'] = 'men'
aliens[0]['name'] = 'et'
aliens[0]['speed'] = 'slow'
print(aliens)


def getIncrement(speed):
    x_increment = 0
    if (speed == 'slow'):
        x_increment = 1
    elif (speed == 'medium'):
        x_increment = 2
    elif (speed == 'fast'):
        x_increment = 3
    return x_increment


aliens[0]['position']['x'] += getIncrement(aliens[0]['speed'])

print(aliens)

for key, value in aliens[0].items():
    print('\nKey:' + key)
    print('Value:' + str(value))


for value in aliens[0].values():
    print(value)