print("\nBoltsAndNuts start")
damage = 0
k1 = int(input("Введите изначальное количество болтов от 100 до 30 тыс. кратное 100: "))  # начальное число болтов
if 100 > k1 or k1 > 30000 or k1 % 100 != 0:
    print("Введите корректное значение.")
else:
    l1 = int(input("Введите процент потерянных болтов от 0 до 100: "))  # процент потерянных болтов
    if 0 > l1 > 100:
        print("Введите корректное значение от 0 до 100.")
    else:
        m1 = int(input("Введите стоимость одного болта от 0 до 100: "))  # стоимость одного болта
        if 1 > m1 > 100:
            print("Введите корректное значение от 0 до 100.")
        else:
            k2 = int(
                input("Введите изначальное количество гаек от 100 до 30 тыс. кратное 100: "))  # начальное число гаек
            if 100 > k2 or k2 > 30000 or k2 % 100 != 0:
                print("Введите корректное значение.")
            else:
                l2 = int(input("Введите процент потерянных гаек от 0 до 100: "))  # процент потерянных гаек
                if 0 > l2 > 100:
                    print("Введите корректное значение от 0 до 100.")
                else:
                    m2 = int(input("Введите стоимость одного болта от 0 до 100: "))  # стоимость одной гайки
                    if 1 > m1 > 100:
                        print("Введите корректное значение от 0 до 100.")
                    else:
                        lost_bolts = k1 / 100 * l1
                        lost_nuts = k2 / 100 * l2
                        # if lost_bolts > lost_nuts:
                        #     damage = lost_bolts * m1 + lost_bolts * m2
                        # elif lost_bolts < lost_nuts:
                        #     damage = lost_nuts * m1 + lost_nuts * m2
                        # else:
                        #     damage = lost_bolts * m1 + lost_nuts * m2
                        remaining_bolts = k1 - lost_bolts
                        remaining_nuts = k2 - lost_nuts
                        if remaining_bolts > remaining_nuts:
                            damage = (remaining_bolts - remaining_nuts) * m1 + lost_bolts * m1 + lost_nuts * m2
                        elif remaining_bolts < remaining_nuts:
                            damage = abs(remaining_bolts - remaining_nuts) * m2 + lost_bolts * m1 + lost_nuts * m2
                        else:
                            damage = lost_bolts * m1 + lost_nuts * m2
                        print(f"Общий ущерб составляет: {damage}")
