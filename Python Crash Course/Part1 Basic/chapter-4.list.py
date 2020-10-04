magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

for value in range(1, 5):
    print(value)

digits = range(1, 100, 3)
print(min(digits))
print(max(digits))
print(sum(digits))


#列表解析
squares = [value**2 for value in digits]

print(squares)