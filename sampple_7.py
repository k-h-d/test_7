a = int(input("数字1："))
b = int(input("数字2："))
while True:
    c=a%b
    if c == 0:
        print(b)
        break
    a=b
    b=c
