# _*_ coding: utf-8 _*_


def get_zui(m, n):
    i = m
    while (m % i != 0) or (n % i != 0):
        i -= 1
    return i


def main(a,b,n):
    zui = get_zui(a, b)
    if zui>n:
        print 0
        return
    num = 1

    while zui * num < n:
        num += 1
    print num-1
    return


if __name__ == '__main__':
    line_1 = raw_input()
    a = int(line_1.split(" ")[0])
    b = int(line_1.split(" ")[1])
    n = int(line_1.split(" ")[2])
    main(a,b,n)
