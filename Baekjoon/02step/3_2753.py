year = int(input())
if ((year%4==0)and(year%100!=0)or(year%400==0)):
        print('1')
else:
    print('0')
    
#year = int(input())
#a = year % 4
#b = year % 100
#c = year % 400
#if ((a==0)and(b!=0)or(c==0)):
#        print('1')
#else:
#    print('0')

#아래 코드가 시간이 더 짧음