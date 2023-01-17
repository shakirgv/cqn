import sys
# CQN ümumi 50 baldır -- davamiyyət - 10; seminar - 20; sərbəst iş - 10; kollokvium - 10 bal
# neçə seminar balı varsa, hamısı toplanılır 2-yə vurulub seminar balının sayına bölünür
# 3 kollokvium balı toplanılır 3-ə bölünür
# qaib limiti -- fənnin saatı 20-yə vurulub 100-ə bölünür (20%) 
# fənnin saatı 30-dursa; 1-3 qaib 9 bal, 4-6 qaib 8 bal 
# fənnin saatı 45-dirsə; 1-5 qaib 9 bal, 6-9 qaib 8 bal 
# fənnin saatı 60-dırsa; 1-6 qaib 9 bal, 7-12 qaib 8 bal 

saat = int(input("Fənn neçə saatdır: "))
limit = (saat * 20) / 100
qaib = int(input("Neçə qaibiniz var: "))
if qaib > limit:
    print("Qaib limitindən kəsilmisiniz!")
    sys.exit()
elif qaib == 0:
    davam = 10
elif ((qaib>=1) and (qaib<=3)) and (saat == 30):
    davam = 9
elif ((qaib>=4) and (qaib<=6)) and (saat == 30):
    davam = 8
elif ((qaib>=1) and (qaib<=5)) and (saat == 45):
    davam = 9
elif ((qaib>=6) and (qaib<=9)) and (saat == 45):
    davam = 8
elif ((qaib>=1) and (qaib<=6)) and (saat == 60):
    davam = 9
elif ((qaib>=7) and (qaib<=12)) and (saat == 60):
    davam = 8
else:
    print("Fənnin saatını yanlış yazmısınız")

seminarBallari = []
seminarSayi = int(input("Neçə dəfə seminar danışmısınız: "))

for n in range(seminarSayi):
    bal = int(input('Seminar ballarınızı yazın (ardıcıl olaraq): '))
    seminarBallari.append(bal)

seminarCemi = sum(seminarBallari)

seminar = (seminarCemi * 2) / seminarSayi

serbest = int(input("Sərbəst iş balınız: "))
kollok1 = int(input("1-ci kollokvium balınız: "))
kollok2 = int(input("2-ci kollokvium balınız: "))
kollok3 = int(input("3-cü kollokvium balınız: "))
kollok = (kollok1+kollok2+kollok3)/3

cqn = (kollok + serbest + davam + seminar)

print(f"Sizin CQN göstəriciniz: {cqn}")