# 数据结构：
# 列表

list2 = [1, 8, 3, 4, 7] 
#print(len(list2))

#append insert pop remove 
list2.append(9) #使用append 添加列表数据
list2.insert(1,7) #使用insert插入数据
list2.insert(2,5) #使用insert插入数据
list2.pop(2) #使用pop删除指定位置的元素
print(list2)

for num in list2:
    if 7 in list2:
        list2.remove(7) #使用remove去除指定元素

print(list2)

# 数据结构：
# 元组 

tuple2 = (1, 3, 5, 7)
t3 = list(tuple2)       #将tuple 转成list
t3.append('world')
print(tuple2[2])
print(t3)

