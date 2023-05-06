


























# def hello(name):
#     print("Привет", name)
# hello("Kurmanbek")
# hello("Beff")

# def test(word:str) -> str:
#     "My testing function"
#     print(word + word)
# test("geeks")
# test(10)

# def mult(num1:int=1, num2:int=1) -> int:
#     print("Ответ:", num1*num2)
# mult(10,10)
# mult(10,20)

# def calculator(num1:int=1, num2:int=1, operator:str='+') -> int:
#     "Simple calculator Python with fuction def"
#     if operator == "+":
#         print("Ответ:", num1+num2)
#     elif operator == "-"
#         print("Ответ:", num1-num2)
#     elif operator == "*":
#         print("Ответ:", num1*num2)
#     elif operator == "/"
#         print("Ответ:", num1/num2)
#     else:
#         print("Такого оператова нету")
# calculator(10,20,"+")
# calculator(10,20,"/")
# calculator(20,30,"-")
# calculator(20,30,"*")
# calculator(10,0,"/")

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Деление на ноль")
   
# try:
#      print(10+ "5")
# except TypeError:
#     print("Ошибка типа данных")

# try:
#     print(10 + 10) 
# except BaseException:
#     print("Code Error")
    
    
# while True:
#     try:
#         num1 = int(input("Number1:"))
#         operator = input("Operator:")
#         num2 = int(input("Number2:"))
#         if operator == "+":
#             print("Ответ:", num1+num2)
#         elif operator == "-":
#             print("Ответ:", num1-num2)
#         elif operator == "*":
#             print("Ответ:", num1*num2)
#         elif operator == "/":
#             try:
#                 print("Ответ:", num1/num2)
#             except:
#                 print("деление на ноль")
#         else:
            
#             print("Такого оператова нету")
#     except ValueError:
#         print("Введите цифры")
            