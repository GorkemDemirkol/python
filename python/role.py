import random
#program döngüsü
#zar oyunu
#eğer kulanıcı onaylarsa
# oyun doğru oldu sürece devam eddecek
oyun=True
while oyun:
    cevap=input("Zar oyunu oynamak ister misiniz? (evet/hayır)")
    cevap=cevap.lower()
    if cevap=="evet":
        #rasgele 2 zar atılacak
        zar1=random.randint(1,6)
        zar2=random.randint(1,6)
        #sonucu yazdır
        print(f"Zar1: {zar1} Zar2: {zar2}")
        print(f"Toplam: {zar1+zar2}")
    elif cevap=="hayır":
        print("Oyunu oynamadınız,iyi günler")
        break
    else:
        print("Geçersiz cevap")


#eğer kullanıcı onaylamazsa
#tekrar oynamak ister misiniz?
#