def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

n = input("Enter number banknotes: ")

if not is_number(n):
    print("Enter not number")
    quit()

n = int(n)

s = input("Enter the amount: ")

if not is_number(s):
    print("Enter not number")
    quit()

s = int(s)

if s <= 0 or n <= 0:
    print("Enter a positive number or number > 0")
    quit()

if s > 5000000 or n >= 100:
    print("s > 5000000 or n >= 100")
    quit()

a = []
for i in range(n):
    d = int(input("Enter banknote: "))
    a.append(d)

a = sorted(a, reverse = True)


r = []
b = 0
for i in a:
    b = s // i
    k = b*i
    s = s - k
    r.append(b)

if s > 0:
    print("impossible")
    quit()
for i in range(n):
    if r[i] >= 1:
        print(r[i], "x", a[i])
