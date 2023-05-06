# дз 1
# l = lambda number: number * number -10
# print(l(10))

# дз 2

# name = ["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina"]
# lam_lam = lambda name : list(set(name))
# print(lam_lam(name))

# дз 3

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lam = list(filter(lambda lister: lister % 2 ==0, numbers))
# print(lam)

# дз 4

# names = ["azat", "zina", "kuma", "anna", "sas"]
# lam = list(filter( lambda poli: poli ==poli[::-1], names))
# print(lam)

# дз 5

# oclock1 = input("Введите первую отметку времени в формате 'чч:мм:сс': ")
# h1, m1, s1 = map(int, oclock1.split(':'))

# oclock2 = input("Введите вторую отметку времени в формате 'чч:мм:сс': ")
# h2, m2, s2 = map(int, oclock2.split(':'))

# end_second1 = h1 * 3600 + m1 * 60 + s1
# end_second2 = h2 * 3600 + m2 * 60 + s2

# end = end_second1 - end_second2

# print(f"Разница между отметками времени: {end} секунд")
