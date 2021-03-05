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

print(a)

b = ''

c = []
m = []

v=0

for i in a:
    b = ord(i)
    c.append(b)

bSort(c)

for z in c:
    print(chr(z), end=' ', )
print("\n")

b = sorted(c, reverse = True)
for k in b:
    print(chr(k), end=' ', )

# for d in c:
#     k = -1 * d
#     m.append(k)
#
# bSort(m)
#
# for y in m:
#     h = -1*y
#     print(chr(h), end=' ', )


