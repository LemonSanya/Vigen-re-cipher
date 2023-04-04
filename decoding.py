def main():
    x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(x)
    a = input().upper()
    b = input().upper()
    result = ''
    i = 0

    if len(b) > len(a):
        z = len(b) - len(a)
        while i < z:
            a = a + a[i]
            i += 1
    i = 0


    while(i < len(b)):
        a1 = x.index(a[i])
        b1 = x.index(b[i])
        k = b1 - a1
        if k > len(x) - 1:
            k = k - len(x)
        result = result + x[k]
        i += 1
    print(result)

if __name__ == main():
    main()