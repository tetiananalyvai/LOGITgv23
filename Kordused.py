#1
print("*** ������ ����� ***")
print()
while True:
    try:
        n=int(input(" ������� ��: "))
        if 1<=n<=9:
            break
    except ValueError:
        print("Viga. Sisesta arv 1-9!")
for i in range(n):
    print(" (\_/)\n (o o)\n / | \*")

#2    
summ=0
for i in range(14+1):
    summ+=i
    
print(summ)

#3
import random   
x=0                                      
a=random.randint(1,100)    
while x<10:
   b=int(input('�����: '))
   if b>a:
       print("������!")
   elif b<a:
       print('������!')
   elif b==a:
       print('�� �������!')
       break    
   x+=1
print('��� �����: ' + str(a))

#4
n1=int(input("������� ����� �����: "))
n2=0

while n1>0:
    digit=n1 % 10
    n1=n1//10

    n2=n2*10
    n2=n2+digit
print('"�������"��� �����:',n2)

5
inputNumber = input('������� �����: ')
numbers = []
i = 0
while i < len(inputNumber):
   number = inputNumber[i]
   if not number.isnumeric():
       continue
   numbers.append(int(number))
   i += 1
n = 0
m = 1
for number in numbers:
   n += number
   m *= number
print(n, m, sep='\n')
    



