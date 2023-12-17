# 03-01 ===================

money = True

if money:
    print('by_taxi')
else:
    print('on_foot')


if "1" not in ["1", '2', '3']:
    print("none")
else:
    print("1")

if 1!=1:
    print('false')
else:
    print('true')

if 1==1:
    pass

# 03-02 ===================

treehit = 0
while treehit < 5:
    treehit = treehit+1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 5:
        print("나무가 넘어갑니다.")


number = 1
while number < 10:
    if number%3 == 0:
        print('%d는 3의 배수입니다.' %number)
    else:
        print('%d는 3의 배수가 아닙니다.'%number)
    number = number + 1    

for number in range(1,9):
    if number%3 == 0:
        print('%d는 3의 배수입니다.' %number)
    else:
        print('%d는 3의 배수가 아닙니다.'%number)

marks = [90, 25, 67, 45, 80]
number = 1
for i in marks:
    if i >= 60:
        print('%d번 학생은 합격입니다.' %number)
        number = number + 1
    else:
        print('%d번 학생은 불합격입니다.' %number)
        number = number + 1

sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

a = [1, 2, 3, 4]
result = [i*3 for i in a if i%2 == 0]
print(result)