print("\nПроверялка строк")
str1 = input("Введите строку 1:\n ")
str2 = input("Введите строку 2:\n ")
str3 = input("Введите строку 3:\n ")

if str1 == str2 == str3:
    print("Все строки идентичны.")
elif str1 == str2:
    print("Строка 1 равна строке 2.")
elif str2 == str3:
    print("Строка 2 равна строке 3.")
elif str1 == str3:
    print("Строка 1 равна строке 3.")
else:
    print("Строки не равны.")
