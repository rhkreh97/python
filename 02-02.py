# 02-3 ==================

a = [1, 2, 3]
b = ['life', 'is', 'too', 'short']

print(a)
print(b)

print(a[0]+a[2])

c = a + b
print(c)

d = [1, 2, 3, ['life', 'is', 'too', 'short']]
print(d[-1][2])

print(a[0:2])

test1 = [1, 2, 3, 4, 5]
print(test1[1:3])

print(a*3)
print(len(a))
print(str(a[0])+"hi")

a[2] = 6
print(a)

del a[0]
print(a)

a.append(4)
a.append([5, 6])
print(a)

del a[-1]
a.sort()
print(a)

a.reverse()
print(a)

print(a.index(2))

a.insert(1, 5)
print(a)

a.append(5)
a.insert(3, 5)
a.remove(5)
print(a)

print(a.pop())
print(a)
print(a.pop(1))
print(a)

a.count(1)
a.extend([5, 6, 7])
print(a)

# 02-4 ===================

t1 = (1, 2, 'a', 'b')

print(t1[0])
print(t1[1:3])

t2 = (3, 4)
print(t1+t2)

test2 = (1, 2, 3)
print(test2+(4,))

# 02-5 ===================

dic = {'name' : 'dohun', 'phone' : '010-3348-4023', 'birth' : '0423'}
dic['grade'] = 'senior'
print(dic)

del dic['grade']
print(dic)

print(dic['name'])
print(dic.keys())
print(list(dic.keys()))
print(list(dic.items()))

print(dic['birth'])
print(dic.get('birth'))
print(dic.get('major'))
print(dic.get('major', '0'))

print("name" in dic)
print('email' in dic)

test3 = {'name':'홍길동', 'birth':'1128', 'age':'30'}
print(test3)

# 02-6 ==============================

set_1 = set([3, 5, 7, 1, 0, 8])
print(set_1)

set_2 = set(['a', 'j', 'k', 'b', 's'])
set_3 = set(['a', 'k', 'j', 'b', 's', 'v'])
print(set_2)
print(set_3)

list_1 = list(set_1)
list_2 = list(set_2)
list_3 = list(set_3)

tuple_1 = tuple(set_1)
tuple_2 = tuple(set_2)
tuple_3 = tuple(set_3)

print(list_1+list_2+list_3)
print(tuple_1+tuple_2+tuple_3)

print(set_1 & set_2)
print(set_2 & set_3)
print(set_2 | set_3)
print(set_2 - set_3)
print(set_3 - set_2)

print(set_2.intersection(set_3))
print(set_2.difference(set_3))
print(set_2.union(set_3))

set_1.add(4)
print(set_1)
set_1.update([4, 5, 6])
print(set_1)
set_1.remove(3)
print(set_1)

# 02-7 ============================

T = True
F = False

print(1 == 1)


if []:
    print('참')
else:
    print('거짓')

if [1]:
    print('참')
else:
    print('거짓')

print(bool('name'))
print(bool(''))

# 02-8 ==================================

print(id(set_1))

a = [1, 2, 3]
b = a[:]

a[1] = 4

print(id(a) == id(b))

from copy import copy
a = [1, 2, 3]
b = copy(a)

print(id(a) == id(b))