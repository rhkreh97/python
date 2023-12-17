# 02-1

a = 123
a = 10e10
a = 3.14

print(a)


a = 3
b = 4
print(a ** b)

print(10*18**2+2*11)

print(7%5)
print(7//5)
print(4/3)

# 02-2

a = "hello"
b = "subin"

print(a+" "+b)

# 02-2-2

a = "="
b = '"My Program"'

print(a*20+"\n"+b+"\n"+a*20)

print(b[4])
print(b[3])
print(b[-1])

c = b[1] + b[4] + b[-3] + b[6]

print(c)

c = b[-11] + b[-6] + b[-2]

print(c)

c = b[4:-1]

print(c)

#====================

c = b[-8:-1]

print(c)

c = b[:12]

print(c)

d = "20231216"

year = d[0:4]
month = d[4:6]
day = d[6:8]

print(year+' '+month+" "+day)

phone = "1047367769"

a = phone[0:2]
b = phone[2:6]
c = phone[6:10]

print(a+b+c)

if len(a)==3:
    if len(b)==3:
        if len(c)==4:
            print('true')
        else:
            print('false')

#=====================================

print("hello %d" %120)

a = "hello %d" %120

a = 10.98
day = 'three'

print("""I ate %f apples.
So I was sick for %s days.""" %(a, day))

print("%-10s | %-10s | %-10s" %("수빈", "도훈", "람강"))

print("%10.4f" %8.15613156112)

print("I eat {apple} apples and {orange} oranges" .format(apple=3, orange=4))

print("{apple:!<10}" .format(apple="hi"))

print(f'{"python":!^12}')


a="2023"
b="12"
C="16"

print("." .join([a,b,C]))

phone .split('-')

print('감사합니다')



print("""|\\_/|
|q p|   /}
( 0 )\"\"\"\\
|\"^\"`    |
||_/=\\\\__|""")