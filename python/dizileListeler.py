ifade="python sınıfı"
print(ifade[10])
ifadeler=ifade*10
print(ifadeler)
print(len(ifade))
cumle="python 1980 lerin sonunda Guido Van Rossum tarafından python geliştirildi"
print(cumle.capitalize())
print(cumle.upper())
print(cumle.lower())
print(cumle.title())
print(cumle.swapcase())
print(cumle.count("python"))
print(cumle.count("a"))
print(cumle.find('a'))
print(cumle.index('a'))
print(cumle.rindex('a'))

print(cumle.startswith("p"))

kelime="python2025"
print(kelime.isalnum())
print(cumle.isalnum())
print(kelime.isalpha())
print(kelime.isdigit())
print(kelime.islower())
space=" "
print(space.isspace())
title="Gorkemli Bir Baslik"
print(title.istitle())
upper="PYTHON"
print(upper.isupper())

center="python"
print(center.center(50))
print(center.center(50,"*"))

expant="python\t programlama\t dili"
print(expant)
print(expant.expandtabs(20))

just="python 2025"
print(just.ljust(50,"-"))
print(just.rjust(50,"-"))

strip="  python  python  "
print(strip.strip())

fill="1234"
print(fill.zfill(10))

d="abcdef"
d2=d[1:3]
print(d2)
d3=d[-4:-1]
print(d3)
d4=d[2:]
print(d4)
d5=d[:3]
print(d5)
d6=d[-3:]
print(d6)
d7=d[:-2]
print(d7)
d8=d[::2]   
print(d8)
sayi="0123456789"
print(sayi[::2])
print(sayi[2:8:2])
print(sayi[::-1])
print(sayi[8:2:-2])#!
print(sayi[5::2])

print(len(sayi))
print(sayi[:len(sayi):2])

paragraf="python dersleri süper\n dersimizde 3 kişi var hoşgeldiniz    "
paragraf2="python dersleri süper"
paragraf3="dersimizde 3 kişi var hoşgeldiniz  "
print(paragraf) 
print(paragraf2)
print(paragraf3)
sembol="\x2c"
print(sembol)
paragraf4="\'metin\'"
print(paragraf4)
paragraf5="\r 'python \r' programlama \r dili \r"
print(paragraf5)


thisList=["apple","banana","cherry"]
thisList.insert(1,"orange")
print(thisList)
thisList.pop(1)
print(thisList)


