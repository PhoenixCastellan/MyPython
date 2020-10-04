

a = [1,2,3,"lvrihui"]
b = a[:]
b[0] = 2
print(a)
print(b)

a.append("lvhf")

print(b)
print(a)


print(list(range(5 ,10)))


for i in range(1,10):
    print(i)


sum = 0
for i in range(10):
    sum +=i
    print(sum)