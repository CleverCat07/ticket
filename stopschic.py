def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def is_fl_or_in(x):
    y = int(x) - x
    if y == 0:
        x = int(x)
    else:
        x = x
    return x

a = input("Введіть перше число: ")
if not is_number(a):
    print("Введіть число!")
    quit()
b = input("Введіть операцію: ")
c = input("Введіть друге число: ")

if not is_number(c):
    print("Введіть число!")
    quit()

a = float(a)
c = float(c)

a = is_fl_or_in(a)
c = is_fl_or_in(c)

k = len(str(a))
y = len(str(c))
v = k-y
if v < 0:
    v = y-k
if v > 0:
    q = " "
    w = ""
    e = ""
    p=""
    for i in range(v-1):
         e = y + k
    q = "-"
    w = "--"
    for i in range(v+1):
        p = q + w
if b == "+":
    v = k - y
    if v < 0:
        print(" ", e,a)
        print("+",c)
    else:
        print(" ", a)
        print("+", e, c)
        print(str(p))
        s = a + c
        s = is_fl_or_in(s)
        print(" ", s)