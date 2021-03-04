import random, string

def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

a = random_char(30)

print (a)

b = ''

c = []
k=0
d=''
m = 0
v = 0

for i in a:
    b = ord(i)
    c.append(b)
    bSort(c)
    k=k+1
    m=m+1
    if k == 30:
        for z in c:
            print(chr(z), end=' ', )
            v=v+1
            if v==30:
                print("\n")
            continue
    if m == 30:
        for y in reversed(c):
            print(chr(y), end=' ', )


