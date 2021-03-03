def data(first_name, last_name, age):
    return {'first_name': first_name,
            'last_name': last_name,
            'age': age}

boys = [data('Vlad', 'Vlasiuk', '13'), data('Orest','Hulenko', '13'), data('Misha', 'Ushkov', '14')]

for boy in boys:
    print(boy["last_name"])



# print(boys_D)
# boys_C = ["Влад","Антон", "Вова", "Вітя"]
#
# boys_B = ["Ярік","Віталік", "Глеб", "Артем", "Вадім"]
#
# boys_A = ["Ігорь","Андрій", "Олег", "Богдан",]
#
# boys_class = [boys_A, boys_B, boys_C, boys_D]
#
# for boys in boys_class:
#     print("Клас")
#     for i in boys:
#        print(i)
#

