import sqlite3
#veri tabanı bağlantısı oluşturma
conn = sqlite3.connect('ornek.db')
cursor=conn.cursor()
# tablo oluşturma
cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS kulanicilar (
id INTEGER PRIMARY KEY AUTOINCREMENT,
isim TEXT NOT NULL,
YAS INTEGER NOT NULL
)
''')
# veri ekleme
cursor.execute('''INSERT INTO kulanicilar (isim,yas) VALUES (?,?)''',('Gorkem',25))
cursor.execute('''INSERT INTO kulanicilar (isim,yas) VALUES (?,?)''',('Mete',35))
cursor.execute('''INSERT INTO kulanicilar (isim,yas) VALUES (?,?)''',('Osman',32))
#değişiklikleri kaydetme
conn.commit()
#veri sorgulama
cursor.execute('''SELECT * FROM kulanicilar''')
kulanicilar = cursor.fetchall()
#sonuçları yazdırma
for kullanici in kulanicilar:
    print(kullanici)
#bağlantıyı kapatma
conn.close()