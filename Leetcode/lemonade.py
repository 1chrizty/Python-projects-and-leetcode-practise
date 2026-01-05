''' Lemonade changes '''

count = 0
a = []
for i in range(0,5):
    b = int(input('enter the values:'))
    a.append(b)
sum1 = 0
sum2 = 0
sum3 = 0


for i in range(len(a)): 
    if a[i] == 5:
        sum1 += 5
    elif a[i] == 10:
        sum2 += 10
        if sum1 >= 5:
            sum1 -= 5
        else:
            count = 1
    elif a[i] == 20:
        sum3 += 20
        if sum1 >= 5 and sum2 >= 10:
            sum1 -= 5
            sum2 -= 10
        else:
            count = 1
    else:
        print('error in values in list')
        count = 1
print( count == 0)

