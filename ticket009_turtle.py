import math as m
import numpy as np
import matplotlib.pyplot as plt

def input_int(s):
    a = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return int(a)
    except ValueError:
        print("isn`t number")
        quit()

print("y = -3x2 - 4x + 20")

a = input_int("Enter a = ")
b = input_int("Enter b = ")
c = input_int("Enter c = ")

y = lambda x: (-3 * x ** 2 - 4 * x + 200)
xs = np.linspace(a, b, c)
plt.plot(xs, [y(x) for x in xs])
plt.show()

for x in xs:
    y = -3 * x ** 2 - 4 * x + 20
    print(x, y)

