# 1

list_01 = {'국어':80, '영어':75, '수학':55}
grade_01 = list(list_01.values())
sum_01 = grade_01[0]+grade_01[1]+grade_01[2]
average_01 = sum_01/3

print(average_01)

# 2

integer_02 = 13
if 13%2 == 0:
    print('짝수')
else:
    print('홀수')

# 3

pin_03 = "881120-1068234"
yyyymmdd_03 = pin_03[:6]
num_03 = pin_03[7:]

print(yyyymmdd_03)
print(num_03)

# 4

pin_04 = "881120-1068234"

print(pin_04[7])

# 5

string_05 = "a:b:c:d"
string2_05 = string_05.replace(':', '#')

print(string2_05)

# 6

list_06 = [1, 3, 5, 4, 2]
list_06.sort()
list_06.reverse()

print(list_06)

# 7

list_07 = ['Life', 'is', 'too', 'short']
result_07 = " ".join(list_07)

print(result_07)

# 8

tuple_08 = (1, 2, 3)
tuple2_08 = tuple_08 + (4,)

print(tuple2_08)

# 9 (solved)

dictonary_09 = dict()

# 10

dictonary_10 = {'A':90, 'B':80, 'C':70}
result_10 = dictonary_10.pop('B')

print(dictonary_10)
print(result_10)

# 11

list_11 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_11 = set(list_11)
list2_11 = list(set_11)

print(list2_11)

# 12 (solved)

lista_12 = listb_12 = [1, 2, 3]
lista_12[1] = 4

print(listb_12)
