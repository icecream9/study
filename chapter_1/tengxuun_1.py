# _*_ coding: utf-8 _*_
import math

num = 0


def main(n, length):
    global num
    if n == 0:
        num += 1
        return
    if length == 2:
        if n == 4:
            num += 2
            return
        elif n == 3:
            num += 1
            return
        elif n == 2:
            num += 2
            return
        elif n == 1:
            num += 1
        else:
            return
    elif length == 1:
        if n == 2 or n ==1:
            num += 1
        return
    main(n - math.pow(2, length-1), length - 2)
    main(n - math.pow(2, length-1) - math.pow(2, length - 2), length - 2)
    main(n - math.pow(2, length - 1), length - 2)


if __name__ == '__main__':
    n = int(raw_input())
    length = int(math.log(n) / math.log(2))
    # print length
    main(n, length+1)
    print num
