#字典

score_list = [0, 1, 2, 3]
score_turple = (0, 1, 2, 3)
scores = {'小明' : 100, '小红' : 95, '小刚' : 99 }
print(scores['小明'], score_list[0], score_turple[0])

# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
scores['小明'] = 65
scores['小红'] = 71
scores.update(小天= 67, 小杰= 85)

for key in scores:
    print(f'{key} : {scores[key]}')

if '小明' in scores:
    print(scores['小明'])

print(scores.popitem())
print(scores.pop('小明'))
print(scores)

scores.clear()
