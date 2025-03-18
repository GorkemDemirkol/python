import qrcode 


data = input("URL'nizi giriniz: ")
file_name = input("Dosya adını giriniz: ")
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)  # QR kodunun boyutunu otomatik olarak ayarlamak için fit=True ekledik
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save(file_name + ".png")

print("QR Code oluşturuldu.")


