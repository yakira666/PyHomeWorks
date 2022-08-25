year = int(input("Укажите год: "))
p = year // 4 == 0 and (year // 100 != 0 or year // 400 == 0)  # осталась доработать
print(year, "год высокосный это -", p)
