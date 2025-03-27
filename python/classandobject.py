class myclass:
    x = 5
p1 = myclass()
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def karsilama(self):
        print("Merhaba",self.name,self.age)
p1=person("Görkem",25)
p2=person("Mehmet",30)
print(p1.name)
print(p1.age),print(p2.name),print(p2.age)

print(p1)
p1.karsilama()

class insanlar:
    def __init__(mySillyObject,name,city):
        mySillyObject.name=name
        mySillyObject.city=city
    def karsilama(abc):
        print("merhaba",abc.name,abc.city)
p3=insanlar("Görkem","Denizli")
p4=insanlar("Mehmet","Ankara") 
p3.karsilama()
p4.karsilama()
del p4.city
class student(person):
    pass
s1=student("Mete",35)
s1.karsilama()
class teacher(person):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.workStartYear=year
    def akrsilama2(self):
        print("Hoş geldiniz",self.name,self.age,self.workStartYear)
t1=teacher("sadullah",25,2020)
t1.akrsilama2()

