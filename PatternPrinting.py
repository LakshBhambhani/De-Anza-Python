# Pattern Printing

num = 1
while num <= 4:
    x = 1
    while x <= num:
        print('*', end ='')
        x += 1
    num += 1
    print('\n', end ='')

num  = 1
print('\n')

n = 3

for i in range(n-1):
    print((n-i) * ' ' + (2*i+1) * '*')
for i in range(n-1, -1, -1):
    print((n-i) * ' ' + (2*i+1) * '*')

print('\n', end= "")

binary = [1, 0, 1, 0, 1, 0, 1]
length = len(binary)

while length >= 3:
    for x in binary:
        print(x, end = '')
    binary.pop()
    binary.pop()
    length = len(binary)
    print('\n', end ='')

print('\n', end ="")

num = 1
while num <= 9:
    x = 1
    while x <= num:
        print(num, end ='')
        x += 1
    num += 1
    print('\n', end ='')

num  = 1
