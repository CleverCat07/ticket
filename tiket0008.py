def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

a = input("Enter a = ")

if not is_number(a):
    print("Enter the number")
    quit()

x = float(a)

if x < 0:
    print("Enter a positive number")
    quit()

b = ''
for i in a:
    b = i + b

c = x-float(b)

print("Перевернуте число: ",str(b))
print(str(a)+"-"+str(b)+"="+str(c))
print("Різниця чисел: ",str(c))




