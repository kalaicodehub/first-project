print('''choices are,
            1.decimal to binary
            2.binary to decimal''')
cho=int(input("\nenter the choice:"))
if cho==1:
    num = int(input('\nenter a number:'))
    g = num
    f = 0
    n = 0
    while num > 1:
        n += 1
        num //= 2
    for i in range(0, n):
        f += (g % 2) * (10 ** i)
        g //= 2

    print("\n",f + (g * (10 ** n)))
elif cho==2:
    num = int(input("\nenter a number:"))
    h = num
    f = 0
    g = 0
    while num > 1:
        g += 1
        num //= 10
    for y in range(0, g):
        f += (h % 10) * (2 ** y)
        h //= 10

    print("\n",f + (h * (2 ** g)))
else:
    print("\nsorry")





