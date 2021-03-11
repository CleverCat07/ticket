from hashlib import sha256

while True:
    print("1 - new \n2 - auth \n3 - exit")
    a = input()
    if a == "3":
        break

    f = open('text.txt')
    nick = input("Введіть нік: ")
    key = input('Enter password: ')
    key = sha256(key.encode('utf-8')).hexdigest()
    if a == "1":
        f = open('text.txt', 'a')
        f.writelines(str(nick) + " ")
        f.writelines(str(key) + '\n')
    elif a == "2":
        users = {}
        with open(r"text.txt", "r") as file:
            for line in file:
                e = line.split()
                users[e[0]]=e[1]
        k = users.get(nick)
        if k == key:
          print("ok")
        elif k == None:
                print("Not find nick")
        else:
            print("password is not ok")
    else:
        print("you need print number (1-3)")
