# _*_ coding: utf-8 _*_


def gcd(a, b):
    if b > a:
        t = b
        b = a
        a = t
    while (a % b):
        temp = a
        a = b
        b = temp % b
    return b

def main(a, b, n):
    zui = a * b / gcd(a, b)
    if zui > n:
        print 0
        return
    num = 1

    while zui * num <= n:
        num += 1
    print num - 1
    return


if __name__ == '__main__':
    line_1 = raw_input()
    a = int(line_1.split(" ")[0])
    b = int(line_1.split(" ")[1])
    n = int(line_1.split(" ")[2])
    main(a, b, n)
