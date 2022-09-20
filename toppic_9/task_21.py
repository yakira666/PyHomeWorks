while (data_kurs := float(input("Введите курс доллара к рублю (0 для выхода): "))) != 0:
    data_dols = int(input("Введите колличество долларов: "))
    print(f"По курсу {data_kurs:.2f} рублей за доллар вы получите {data_dols * data_kurs:,.2f}\n")
