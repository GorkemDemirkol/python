import pywhatkit
from datetime import datetime
import os

phone_number=input("telefon numaranızı giriniz: ")
massage=input("mesajınızı giriniz: ")
photo_path=os.path.normpath(r"C:\Users\d-e-m\Pictures\Stealth_1920x1080.jpg")

saat=int(input("saati giriniz: "))
dakika=int(input("dakikayı giriniz: "))

# pywhatkit.sendwhatmsg(phone_number,massage,saat,dakika)

# pywhatkit.sendwhatmsg_instantly(phone_number, massage, tab_close=True)

pywhatkit.sendwhats_image(phone_number, photo_path, massage)
print("mesajınız gönderildi")
