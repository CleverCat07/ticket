def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def result(x, n):
     return "By " + str(n) + " months will be " + str(x) + " rabbits."

n = input("Enter number months: ")

if not is_number(n):
    print("Enter not number")
    quit()

k = input("Enter number rabbits which are eaten by a monster for a month: ")

if not is_number(k):
    print("Enter not number")
    quit()

n = int(n)
k = int(k)

if k < 0 and n < 0:
    print("Enter a positive number or number > 0")
    quit()
elif n > 100 or k > 10000:
    print("k should be < 10000 and n < 100")
    quit()

c = 1
for i in range(n):
    c = 2*c
    if k < c:
        c = c - k

print(result(c, n))
