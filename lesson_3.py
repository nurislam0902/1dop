#Условия if, else, elfi. List - Список
# number = int(input("Введите число:"))
# if number % 2 ==0:
#     print(number,"четный")
# else:
#     print(number, "нечетный")

# age = int(input("Введите свой возраст:"))
# if age < 13:
#     print("Вы не можете пользоапться нашей программой ")
# elif age >=13 and age <= 40:
#     print("Добро пожаловать")
# else:
#     print("Error")
    
#Логические операторы or, and, in, not in
# logen = input("Logen:")
# password = input("Password")
# if logen == 'geeks' and password == 'geeks2023':
#     print("Welcome")
# else:
#     print("Incorrect login or password")

# word = 'Geeks'
# letter = 'G'
# if letter in word:
#     print(letter,"есть в слове", word)
# else:
#     print(letter,"нету в слове",word)

# names = 'Nurdolot Adilet Nursultan Beka'
# find_name = input("Find: ")
# if find_name not in names:
#     print(find_name,' не найти')
# else:
#     print(find_name,'найден')

#Lists - списки
#int, str, float, bool, list
# name1 = 'Nurbolot'
# name2 = 'Kurmanbek'
# name3 = 'Askhat'
# name4 = 'Beksultan'

# names = ['Nurbolot', 'Kurmanbek', 'Askhat', 'Beksultan']
#             #0             #1        #2         #3
# print(names)
# print(names[2][0])
# print(names[1])
# print(names[1:3])
# print(names[::2])

numbers = [1,2,3,4,5,6,7]
print(numbers)
numbers.append(8)
print(numbers)
numbers.append(9)
print(numbers)
numbers.remove(3)
print(numbers)
numbers[0] = 'one'
print(numbers)

it_company = ['Google', 'Meta', 'Microsoft']
it_company.append('Tesla')
print(it_company)
it_company.insert(0,'Geeks')
print(it_company)
it_company.pop(2)
print(it_company)
print(it_company.index('Tesla'))

nums = [10,1,2,212,3,4,5,11]
nums.sort()
print(nums)

it_company = ['BWM', 'TESLA', 'SUPRA','TOYOTA','SUZUKI','NISSAN','MAZDA','MERSEDES','MAYBACH','OPEL','PORSCHE','SUBRU','LEXUS','JEEP','FORT']
print(it_company.index('TESLA', 'SUPRA','TOYOTA','SUZUKI','NISSAN','MAZDA',))
print(it_company)



my_list = [1,2,3,4,5,6,7]
my_list.reverse()
print(my_list)