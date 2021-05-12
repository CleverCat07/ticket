from turtle import *
a = float(input("Одна сторона квадрату: "))
b = float(input("Збільшення сторони: "))
for k in range(4):
    for i in range(4):
        forward(a)
        right(90)
    a = a + b
    up()
    left(90)
    forward(10)
    down()