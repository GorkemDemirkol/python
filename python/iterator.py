myTapiler=("elma","armut","kiraz","karpuz")
myIt=iter(myTapiler)
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
for x in myTapiler:
    print(x)

myStr="Görkem"
myIt2=iter(myStr)
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))
print(next(myIt2))

class myNumbers:
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
       
        if self.a<=1000:
            x=self.a
            self.a+=5
            return x
        else:
            raise StopIteration
myclass=myNumbers()
myiter=iter(myclass)
for i in myiter:
    print(i)
