bicyle = ['forver', 'phoenix', 'giant', 'merida']

print(bicyle[-1])

print(bicyle)

bicyle[3] = 'ducati'

print(bicyle)

bicyle.append("merida")

print(bicyle)

bicyle.insert(0, 'mountain')
print(bicyle)

bicyle.remove("ducati")

print(bicyle)

bicyle.pop(1)
print(bicyle)

bicyle.insert(0, 'mountain')
print(bicyle)

bicyle.remove('mountain')
print(bicyle)

#del bicyle[0]

print(sorted(bicyle))


print(bicyle)
bicyle.sort()
print(bicyle)

bicyle.sort(reverse=True)
print(bicyle)

bicyle.reverse()
print(bicyle)

print(len(bicyle))