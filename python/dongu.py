# amount=int(input("alınan miktarı girin: "))
# item_typ=input("alınan ürünün türünü giriniz: ")
# try:
#     amount=int(input("alınan miktarı girin: "))
#     item_typ=input("alınan ürünün türünü giriniz: ")
# except:
#     print("ürün miktarını tamamını girin: ")
# parts_nummber=int(input("parça sayısını girin"))
# parts_percentage=((amount -parts_nummber)/amount)*100
# try:
#     itemCost=4
#     itemPrice=5
#     amount=int(input("toplam miktarı girin: "))
#     item_type=input("ürün tipini girin: ")
#     parts_nummber=int(input("parça sayısını girin"))
#     parts_percentage=((amount-parts_nummber)/amount)*100
#     revenue=itemPrice*parts_nummber
#     cost=itemCost*parts_nummber
#     profit=revenue - cost
#     print("kalan miktarı yüzdesi: ",parts_percentage)
#     print("sipariş edilen miktar: ",parts_nummber)
#     print("elde edilen kar: ",revenue)
#     print("maliyet: ",cost)
#     print("kar: ",profit)

# except ValueError:
#     print("miktar tam sayı olmalı")
# except ValueError:
#     print("stokta ürün bulunamadı")
# finally:
#     print("program tamamlandı")

def paraCek(bakiye,cekiecek_miktar):
    if cekiecek_miktar<=0:
        raise ValueError("çekilecek miktar 0 dan büyük olmamalı")
    if cekiecek_miktar>bakiye:
        raise ValueError("yetersiz bakiye")
    if cekiecek_miktar>10000:
        raise ValueError("günlük çekim limiti aşıldı")
    return bakiye-cekiecek_miktar

try:
    bakiye=100000
    print(f"Hesap bakiyeniz: ",bakiye," Tl")
    miktar=int(input("çekmek istediğiniz miktarı girin: "))
    yeniBakiye=paraCek(bakiye,miktar)

    print(f"işlem başarılı")
    print(f"çekilen miktar: ",miktar,"Tl")
    print(f"hesap bakiyeniz: {yeniBakiye} Tl")
except ValueError as hata:
    print("hata oluştu: ",hata)
finally:
    print("işlem sonlandırıldı")
