#字符串操作

s1 = '\141\142\143\x61\x62\x63'
s2 = r'\n\\hello world \n'
print(s1, s2, end = '')

#使用slice切片操作字符串
s3 = 'sony panasonic honeywell tesla'
print(s3[14:24])
print(s3[14:24:2])

#使用字符串提供的方法完成字符串的格式
a, b = 1, 3
print('{0} * {1} = {2}'.format(a, b ,a*b))

#python3.6以后，格式化字符串可以在字符串前加上字母f
print(f'{a} * {b} = {a * b}')

