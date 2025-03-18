import random
tutulan=random.randint(1,10)
hak=3
while hak>0:
    tahmin=int(input("1 ile 10 araası bir tahminde bulununuz: "))
    if hak>0:
        if tutulan==tahmin:
            print("Tebrikler, doğru tahmin")
        elif tutulan<tahmin:
          print("Daha küçük bir sayı giriniz")
        elif tutulan>tahmin:
            print("Daha büyük bir sayı giriniz")
        elif tahmin>10 or tahmin<1:
            print("1 ile 10 arası bir sayı giriniz")
        else:
            print("Geçersiz tahmin")
       
        hak-=1
        print("Kalan hakkınız: ",hak)

else:
    print("Hakkınız bitti")
    print("Tutulan sayı: ",tutulan)

