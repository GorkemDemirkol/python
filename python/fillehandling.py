import os
f=open("deneme.txt","r")
# print(f.read())
# print(f.readline(2))
for x in f:
    print(x)
f.close()
f=open("deneme.txt","a")
f.write("Merhaba")
f.close()
f=open("deneme.txt","r")
print(f.read())
f.close()
f=open("deneme2.txt","w")
f.write("Bu alan write ile yazıldı")
f.close()
f=open("deneme2.txt","r")
print(f.read())
f.close()
os.remove("deneme2.txt")
if os.path.exists("deneme2.txt"):
    os.remove("deneme2.txt")
else:
    print("Dosya bulunamadı")