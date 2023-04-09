
def get_money():
    valid_input = False
    while not valid_input:
        try:
            money = float(input("Vəsait: "))
            valid_input = True
        except ValueError:
            print("Xəta! Məbləğ daxil et.")
    return money

def set_money(money):
    return round(money, 2)



def film_al(selection_film, saat_araligi, mebleg):
    meblegg = set_money(mebleg)
    if selection_film == 1:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 18
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif selection_film == 2:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 20
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif selection_film == 3:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 15
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif selection_film == 4:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 10
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
        else:
            print("Xəta!")
    elif selection_film == 5:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 10
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    elif selection_film == 6:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 10
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    elif selection_film == 7:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 8
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    elif selection_film == 8:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 12
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    elif selection_film == 9:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 15
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    elif selection_film == 10:
        if saat_araligi == 1 or saat_araligi == 2:
            qiymeti = 10
            if mebleg >= qiymeti:
                mebleg -= qiymeti
                print("Film uğurla alındı. Qalıq pulunuz:", set_money(mebleg), "AZN")
            else:
                print("Kifayət qədər vəsait yoxdur!")
    
    else:
        print("Xəta! Seçdiyiniz film mövcud deyil.")
        exit()


