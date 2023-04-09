from genclik_mall import *
from gence_mall import *
from aygun_mall import *
from iyirmisekkiz_mall import *
from deniz_mall import *
from movie import *
from money import *
from human import Worken, Person
from mall import *
from datetime import datetime, date

# WORKER AND PERSON
print("""
    Write your personal information !
    _

    Mall da iscisiz ? - 1
    Musterisiniz ? - 2
    """
)

persona_selection = int(input('1 or 2: '))
try:
    if persona_selection == 1:
        print(Worken.who())
    elif persona_selection ==2:
        print(Person.who())
    else:
        exit('daxil edtiyiniz secim movcud deyil!!!')
except ValueError:
    exit("Yalniz reqem daxil edile bilersiz!!!")


print(
    """Getmek istediyiniz Mall secin!
    _
    Genclik Mall - 1
    Aygun Mall - 2
    28 Mall - 3 
    Deniz Mall - 4
    Gence Mall - 5
    """)

selection_mall = int(input("Mall sec: "))

aygun = Aygun("29 Sakit Qocayev, Bakı", "3", "3")
gence = Gence("Heydər Əliyev prospekti 433, Gence", "5", "4")
deniz = Deniz("26a Neftçilər Prospekti, Bakı", "5", "5")
genclik = Genclik("14 Fətəli Xan Xoyski, Bakı", "4", "3")
iyirmisekkiz = Iyirmisekkiz("Azadlig avenu 15a/4 Baku AZ, Bakı", "5", "5")

# MALL-a GIRIS SAATLARI
a = datetime.now()
today = date.today()
timee = a.strftime("%H:%M:%S")
open = 10
close = 23

print("Giris Saati: ", today, timee)

if open <= a.hour < close:
    print("Mall Aciqdi")
elif a.hour <= open:
    exit ("Mall baglidi")
elif a.hour >= close:
    exit("Mall baglidi")

# YAS-in DAXIL EDILMESI
age = int(input('Yasinizi daxil edin: '))
if 12 <= age:
    print('Mall daxil ola bilersiniz')
else:
    exit('Giris qadagandi!!!')

# VAKSIN SERTIFIKAT
c19 = input("COVID-19 vaksin sertifitikatiniz var? Eger vaksin sertifitikaniz var, 'Active' sozunu daxil edin: ")


if c19 == "Active":
    print("Ugurlu")
elif c19 == "Noactive":
    exit("Eytibarsiz!!!")
else:
    exit("Soz duzgun daxil edilmeyib!!!")



# MALL ADLARI VE INFO-lari
if selection_mall == 1:
    print(genclik.info())
elif selection_mall == 2:
    print(aygun.info())
elif selection_mall == 3:
    print(iyirmisekkiz.info())
elif selection_mall == 4:
    print(deniz.info())
elif selection_mall == 5:
    print(gence.info())
else:
    exit("Daxil etdiyiniz nomreli Mall movcud deyil")





# FILMLER Listi ve Secim
print(
    """
    Baxmaq istediyiniz filmi secin. Movcud film siyahisi:

    Forsaj-10 - 1
    Spider-Man - 2
    AVATAR:Su yolu - 3
    Breaking-Bad - 4
    Iron-MAn - 5
    Maze-Runner3 - 6
    Need-For-Speed - 7
    Avengers Endgame - 8
    The Last of Us - 9
    Star Wars - 10
    
    """
)

selection_film = int(input('Baxmaq istediyiniz filmin nomresini daxil edin: '))

series1 = Forsaj_10("Farsaj-10", "Louis Leterrier", 2023, "Adventure, Drama, Fantasy", 8.7,"2h 30m", Hours('10', '12', '12', "14"), 18 )
series2 = Spider_man("Spider-Man: No Way Home", "Jon Watts", 2021, "Fantasy", 8.2, "2h 28m",Hours('10', '12', '12', "14"), 20 )
series3 = Avatar("Avatar: The Way of Water", "James Cameron", 2022, "Adventure, Drama, Fantasy", 7.7, "3h 12m",Hours('10', '12', '12', "14"), 15 )
series4 = Breaking_bad("Breaking-Bad", "Vince Gilligan", 2008, "Adventure, Fantasy", 9.5, "49 minute",Hours('10', '12', '12', "14"), 10 )
series5 = Iron_man("Iron-man 3", "Shane Black", 2013, "Fantasy, Action", 6.8, "2h 10m",Hours('10', '12', '12', "14"), 10 )
series6 = Maze_Runner_3("Maze Runner 3", "Wes Ball", 2014, "Adventure, Fantasy", 6.8, "1h 53m",Hours('10', '12', '12', "14"), 10 )
series7 = Need_for_speed("Need For Speed", "Scott Waugh", 2014, "Action, Thriller", 6.4, "2h 12m",Hours('10', '12', '12', "14"), 8,)
series8 = Avengers_Endgame("Avengers Endgame", "Anthony Russo vs Joe Russo", 2019, "Adventure, Drama, Action", 8.4, "3h 1m",Hours('10', '12', '12', "14"), 12)
series9 = The_last_of_us("The Last of Us", "Neil Druckmann vs Craig Mazin", 2023, "Adventure, Drama, Action", 8.9, "50 minute",Hours('10', '12', '12', "14"), 15 )
series10 = Star_Wars("Star Wars", "Jennifer Corbett vs Dave Filoni", 2021, "Adventure, Action, Animation", 7.8, "2h 10m",Hours('10', '12', '12', "14"), 10)



if selection_film == 1: 
    print(series1.info())
    print(series1.year_info())  
    print(series1.rating_info())
elif selection_film == 2:
    print(series2.info())
    print(series2.year_info())  
    print(series2.rating_info())
elif selection_film == 3:
    print(series3.info())
    print(series3.year_info())  
    print(series3.rating_info())
elif selection_film == 4:
    print(series4.info())
    print(series4.year_info())  
    print(series4.rating_info())
elif selection_film == 5:
    print(series5.info())
    print(series5.year_info())  
    print(series5.rating_info())
elif selection_film == 6:
    print(series6.info())
    print(series6.year_info())  
    print(series6.rating_info())
elif selection_film == 7:
    print(series7.info())
    print(series7.year_info())  
    print(series7.rating_info())
elif selection_film == 8:
    print(series8.info())
    print(series8.year_info())  
    print(series8.rating_info())
elif selection_film == 9:
    print(series9.info())
    print(series9.year_info())  
    print(series9.rating_info())
elif selection_film == 10:
    print(series10.info())
    print(series10.year_info())  
    print(series10.rating_info())  

# Seans
print("""
Choices:
1 ) 10 - 12
2 ) 12 - 14

""")   

try:
    saat_araligi = int(input("Seç: "))
    if selection_film == 1:
        if saat_araligi == 1:
            print("Forsaj-10 filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 18 AZN")
        elif saat_araligi == 2:
            print("Forsaj-10 filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 18 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 2:
        if saat_araligi == 1:
            print("Spider-Man: No Way Home filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 20 AZN")
        elif saat_araligi == 2:
            print("Spider-Man: No Way Home filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 20 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 3:
        if saat_araligi == 1:
            print("Avatar: The Way of Water filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 15 AZN")
        elif saat_araligi == 2:
            print("Avatar: The Way of Water filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 15 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 4:
        if saat_araligi == 1:
            print("Breaking-Bad filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 10 AZN")
        elif saat_araligi == 2:
            print("Breaking-Bad filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 10 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 5:
        if saat_araligi == 1:
            print("Iron-man 3 filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 10 AZN")
        elif saat_araligi == 2:
            print("Iron-man 3 filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 10 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 6:
        if saat_araligi == 1:
            print("Maze Runner 3 filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 10 AZN")
        elif saat_araligi == 2:
            print("Maze Runner 3 filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 10 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 7:
        if saat_araligi == 1:
            print("Need For Speed filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 8 AZN")
        elif saat_araligi == 2:
            print("Need For Speed filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 8 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 8:
        if saat_araligi == 1:
            print("Avengers Endgame filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 12 AZN")
        elif saat_araligi == 2:
            print("Avengers Endgame filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 12 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 9:
        if saat_araligi == 1:
            print("The Last of Us filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 15 AZN")
        elif saat_araligi == 2:
            print("The Last of Us filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 15 AZN")
        else:
            print("Xəta!")
            exit()
    elif selection_film == 10:
        if saat_araligi == 1:
            print("Star Wars filmi mövcud seans: 10 - 12")
            print("Filmin mövcud qiyməti: 10 AZN")
        elif saat_araligi == 2:
            print("Star Wars filmi mövcud seans: 12 - 14")
            print("Filmin mövcud qiyməti: 10 AZN")
        else:
            print("Xəta!")
            exit()
except ValueError:
    print("Xəta!")
    exit()


print("Seçiminizdən əminsinizsə, 'Yes'. deyilsizse 'No' yazın: ")


all_filmi = input("Seç: ")
if all_filmi == "Yes":
    pass
elif all_filmi == "No":
    print("Siz seciminizi deyisdiz!")
    exit()
else:
    print("Ancaq Yes-No seçimi et.")
    exit()


try:
    mebleg = int(input("Vəsait girin: "))
except:
    print("Yalnız qiymət daxil edə bilərsən!")
    exit()
    
film_al(selection_film, saat_araligi, mebleg)

