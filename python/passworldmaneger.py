from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key
master_password = input("Password girişi yapınız: ")
key = load_key()
fer = Fernet(key)

def goruntuleme():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            if not data:
                continue
            user,password=data.split("|")
            print("kullanıcı adı:", user, "şifre:", fer.decrypt(password.encode()).decode())

def ekleme():
    name=input("kulanıcı adı: ")
    password=input("şifre: ")
    with open("passwords.txt","a") as f:
        f.write(name+" |"+fer.encrypt(password.encode()).decode() +"\n")
while True:
    mode=input("mevcut şifrenizi görüntülemek için G değiştirmek için E çıkmak için Q tuşuna basınız : " ).upper()
    # programdan çıkış yapma
    if mode=="Q":
        print("programdan çıkılıyor,iyi günler")
        break
   # görüntüleme 
    if mode=="G":
        goruntuleme()
     # değiştirme(eklemek değiştirmek)
    elif mode=="E":
        ekleme()
    else:
        print("geçersiz işlem")
        continue