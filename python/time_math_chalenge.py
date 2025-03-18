import random
import time 
operators = ['+', '-', '*']
min_operands = int(input("istediğiniz işleme aralığı için en düşük sayıyı giriniz: "))
max_operands = int(input("istediğiniz işleme aralığı için en yüksek sayıyı giriniz: "))
total_problems = int(input("kaç soru çözmek istersiniz: "))

def ganerate_problem():
    left= random.randint(min_operands,max_operands)
    right= random.randint(min_operands,max_operands)
    operator=random.choice(operators)
    ques=str(left)+operator+str(right)
    answer=eval(ques)
    return ques, answer
strat_time=time.time()

wrong=0
input("sorulara başlamak için enter tuşuna basınız")
print("-----------------------------------")
for i in range(total_problems):
    ques,answer=ganerate_problem()
    while True:
        guss=input("problem #"+str(i+1)+" :"+ques+"=")
        if guss==str(answer):
            print("doğru")
            break
        else:
            wrong+=1
            print("yanlış")
            continue
end_time=time.time()
total_time=end_time-strat_time
print("-----------------------------------")
print("toplam doğru sayısı:",total_problems-wrong)
print("toplam yanlış sayısı:",wrong)
print("toplam süre:",round(total_time,2),"saniye")