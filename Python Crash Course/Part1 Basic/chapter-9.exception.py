try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")
while True:
    f_num = input("\nFirst number:")
    if f_num.lower() == 'q':
        break
    s_num = input("\nSecond number:")
    if s_num.lower() == 'q':
        break
    try:
        answer = int(f_num) / int(s_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)