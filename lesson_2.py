#Строка,методы строк
# language="Python"
# courses="Geeks"
# print(language + "" + courses) #Конкатинация
# print(language, courses)

# example_str_one ='Hello.I\'m python developer'  
# print(example_str_one)

# example_str_two = "Hello.I'm python developer\nI'm work in Geeks"
# print(example_str_two)

# example_str_three="""Hello. I'm backend developer
# I'm work in Geeks"""
# print(example_str_three)

# example_str_four = '''Hello. I'm backend developer
# I'm work in Geeks'''
# print(example_str_four)

# name = input("Ваше имя:")
# print("Здраствуйте",name)

# num1 = int(input("Первое число:"))
# num2 = int(input("Второе число:"))
# print(num1*num2)

# coureses ="Geeks"
#            #01234
# print(coureses[0])
# print(coureses[3])
# print(coureses[-5])
# print(coureses[0] + coureses[1] + coureses[2] + coureses[3])
# print(coureses[0:4]) #Срезы, последний инденс не учитывается
# print(coureses[2:5])
# print(coureses[::2])

# name = "nurboLOT" #Nurbolot
# print(name.title())
# print(name.lower())
# print(name.upper())

# #Условия if, else, elif
# print(10 == 20)
# print(2 == 2)

# print(2 != 3)
# print(100 != 100)

# print(3 > 5)

# print(30 > 10)
# print(10 > 30)

# print(10 <= 10)
# print(10 <= 1)

# print(50>=50)
# print(40 >= 5)

# num1=10
# num2=20
# if num1 > num2:
#     print("Первое число больше")
# else:
#     print("Второе число больше")

login = input("Login: ")
password = input("Password: ")
if password == "geeksstudents":
    if login == "geeks":
        print("Welcome")
    else:
        print("Incorrect login")
else:
    print("Incorrect")