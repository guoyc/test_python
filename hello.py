print('hello, world')
print('hello','world')
print('3 * 2 =', 3 * 2)
# name = input('fuck you boy tell me your name');
# print('hey', name);
print(r'\t\t\t')
print('''line1
... line2
... line3''')
print(ord('傻'))
print(chr(20667))
s1 = 72
s2 = 91
print('成绩上升了 %.1f%%' % ((s2 - s1) * 100 // s1))
a = ['多拉多', '漓江塔', '66号公路']
print(len(a))
print(a[0])
# 负数代表去倒数第几个
print(a[-1])
# pop()删除末尾元素，加参数是删除特定位置的元素
# print(a.pop(1))
# list的元素可以不同
# tuple跟list不同的地方,tuple不可变(每个元素的指向不变)
t = ('1', '2', '3')
# 执行的时候会出错
# t.append('4')
print(t)
# 当tuple只有一个元素的时候也要('1',)这么写，避免歧义
age = 20
# 缩进代表代码块，一定要注意if和else需要有:冒号
if age>=18:
    print('fuck you ')
else:
	print('not fuck you ')
#elif 是else if的缩写
# for in循环有点像java的foreach循环
for name in a:
    print(name)
#while循环跟java的while也差不多
a = 1
sum = 0
while a <= 100 :
    sum = sum + a
    a = a + 1
print(sum)
d = {'66':'公路','76':'号'}
print(d['66'])
print('86' in d)
print(d.get('86', None))
# 添加一个元素
d['86'] = 'ae'
print(d)
# 删除一个元素
d.pop('86')
print(d)
# 定义一个set
s = set([1,2,3,4])
s2 = set([1,2,3])
# 可以直接取并集交集等
# s | s2
print(s & s2)
