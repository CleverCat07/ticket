k=0
for el in range(32, 129):
     print(chr(el),  end=' ')
     k=k+1
     if k == 10:
         print("\a")
         k=0