for i in range(0, 151):
    print(i)

for i in range(5,1001,5):
    print(i)

for i in range(0 ,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)

for i in range(2018,0,-4):
    print(i)

lownum = 2
highnum = 9
multnum = 3

for i in range(lownum,highnum + 1):
    if i % multnum == 0:
        print(i)