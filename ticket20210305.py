import random

def random_number():
    return random.randint(0, 110)

y = 0
x = 0
k = []
c =''
for i in range(5):
    k.append(random_number())
    c = c + "," + str(k[i]) + ","

print(k)

k = list(set(k))

for el in k:
    a = c.count("," + str(el) + ",")
    if a > 1 and y > 1:
        x = a
    if a > 1 and y == 0:
        y = a


if y == 5:
    print("poker")
elif y == 4:
    print("four of a kind")
elif x == 3 and y == 2 or x == 2 and y == 3:
    print("full house")
elif y == 3:
    print("three of a kind")
elif y == 2 and x == 2:
    print("two pairs")
elif y == 2:
    print("one pair")
else:
    print("all different")


