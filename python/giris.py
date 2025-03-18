# print("hello world")
# x=5
# y="Gorkem"
# gorkem="görkem"

# a=int(3)
# b=str(3)
# c=float(3.00444)
# sonuc=a+c
# print(sonuc)
# x,y,z="görkem","osman","mete"
# print(x)
# print(y)
# print(z)
# print(x,y,z)

# x="1"
# y="2"
# z="3"
# print(x+y+z)

# x=1
# y=2
# z=3
# print(x+y+z)

# a=3
# def myFunc():
#     print(15+a) 
# myFunc()

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


# print("görkem \"python ı sever\"")

# print('Görkem "python ı sever"')

# userName=input("kulanıcı adını giriniz:  ")
# print("Kulanıcı adınız : ",userName)
# password=int(input("Şifrenizi girin: "))
# print("şifreniz: ",password )


# A_kenari_uzunluk=float(input("A kenar uzunluğunu giriniz: "))
# B_kenari_uzunluk=float(input("B kenar uzunluğunu giriniz: "))

# hypo=(A_kenari_uzunluk**2+B_kenari_uzunluk**2)**.5
# print("hippotenüs uzunluğu : ",hypo)

# print("1=1 eşit mi",1==1)
# print("1=1 eşit mi",1==2)
# print("1<2 eşit mi",1<2)
# print("1<2 eşit mi",1>2)
# print("1>=2 eşit mi",1>=2)
# print("1<=2 eşit mi",1<=2)
# print(bool(""))
# print(bool("görkem"))

# personel=True
# satinAlma=False
# print(personel or satinAlma)
# print(personel and satinAlma)

tren_saatleri=15.00
bilet_fiyati=50
bütce=float(input("cebinizdeki parayı girin(Tl): "))
zaman=float(input("Lütfen gideceğiniz saati girin: "))
if tren_saatleri>zaman and bütce>=bilet_fiyati:
    print("trenin kalkış saatine kalan:  ",(tren_saatleri-zaman),"saat","cebinizde kalan para: ",(bütce-bilet_fiyati),"Tl" )
elif tren_saatleri>zaman and bütce<bilet_fiyati:
    print("paranız yetersiz")
elif tren_saatleri<zaman and bütce>=bilet_fiyati:
    print("paranız yeterli ancak en yakın tren yarın")
elif tren_saatleri<zaman and bütce<bilet_fiyati:
    print("bütçe yetersiz en yakın tren yarın")
