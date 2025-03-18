import qrcode

data = input("url'nizi giriniz:")
file_name = input("Dosya adını giriniz:")
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)  
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save(file_name + ".png")
print("QR Code oluşturuldu.")