def main():
    x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(x)
    a = input().upper()
    b = input().upper()
    result = ''
    i = 0
    a = ''.join(a.split(' '))
    if len(b) > len(a):
        z = len(b) - len(a)
        while i < z:
            a = a + a[i]
            i += 1
    i = 0


    while(i < len(''.join((b).split(' ')))):
        a1 = x.index(a[i])
        b1 = x.index(''.join(b.split(' '))[i])
        k = b1 - a1
        if k > len(x) - 1:
            k = k - len(x)
        result = result + x[k]
        i += 1

    result = list(result)
    b = list(b)
    i = 0

    for q in b:
        if q == ' ':
            result.insert(b.index(q) + i, ' ')
            b.pop(b.index(q))
            i += 1
    print(''.join(result).capitalize())

if __name__ == main():
    main()