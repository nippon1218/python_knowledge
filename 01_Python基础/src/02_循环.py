#求0～100的和

'''
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
'''

#求0～x的和 for 循环实现
def sum_for_realize(x) :
    sum = 0
    if x < 1 :
        return 0
    for i in range(0, x + 1):
        sum += i
    return sum

#求0～x的和 while 循环实现
def sum_while_realize(x) :
    sum = 0
    i = 0
    if x < 1 :
        return 0
    while i <= x:
        sum += i
        i += 1
    return sum
   
print(sum_while_realize(1))

