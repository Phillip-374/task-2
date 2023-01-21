f=open('Perepis.txt','r')


print('1 - Вывести людей младше 1978; 2 - Вывести людей в диапозоне лет ')
a=int(input())
if a==1:
    for i in f:
        date=i[-11::][-5::]
        if int(date)<1978:
            print(i.split(' ')[0])
elif a==2:
    start=int(input())
    stop=int(input())
    for i in f:
        date=i[-11::][-5::]
        if int(date)>start and int(date)<=stop:
            print(i)