# 3-01(solved)

# 3-02

result_02 = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        result_02 = result_02 + i
    i = i + 1

print(result_02)

# 3-03

i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

# 3-04
    
for i in range(1, 101):
    print(i, end=" ")
end = '\n'

# 3-05

list_05 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total_05 = 0
for score_05 in list_05:
    total_05 += score_05
average_05 = total_05/len(list_05)
print(average_05)

# 3-06

list_06 = [1, 2, 3, 4, 5]
result_06 = []
for i in list_06:
    if i%2 != 0:
        result_06.append(i*2)
print(result_06)

list_06 = [1, 2, 3, 4, 5]
result_06 = [i*2 for i in list_06 if i%2 != 0]
print(result_06)