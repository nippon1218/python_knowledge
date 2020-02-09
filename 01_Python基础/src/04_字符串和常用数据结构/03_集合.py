#集合

print('----part 1---------')
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}  #use {} 
print(set1)
print('Length =', len(set1))

# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 5 == 0 or num % 18 == 0}
print(set4)

print('----part 2---------')
set1.add(4) #add添加新的集合元素
set1.add(5)
set2.update([11, 12])   #使用upodate更新集合
set1.discard(2)         #删除2(即使不存在也不会报错)
if 4 in set2:
    set2.remove(4)      #使用discard和remove都能删除，若没有指定的元素，remove会报错，而discard不会
print(set1, set2)
print(set3.pop())       #随机的移除一个元素 
print(set3)

print('----part 3---------')
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)  #交集
#print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

