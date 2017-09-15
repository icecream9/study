# _*_ coding: utf-8 _*_
import math


if __name__ == '__main__':
    n = int(raw_input())
    line_2 = raw_input()
    lis = line_2.split(" ")
    num = 0
    liss = []
    lisq = []
    for ii in range(0,n):
        if int(lis[ii]) % 7:
            lisq.append(lis[ii])
        else:
            liss.append(lis[ii])
    if lisq.__len__() == 1:
        num += 1
    elif lisq.__len__() > 1:
        num += lisq.__len__() * (lisq.__len__()-1)
    for i in range(0, len(liss)):
        one = int(liss[i]) % 7

        for j in range(0, i):

            if (int(liss[j]) + one * math.pow(10, len(liss[j]))) % 7 == 0:
                num += 1
        for j in range(i + 1, n):

            if (int(liss[j]) + one * math.pow(10, len(liss[j]))) % 7 == 0:
                num += 1
    print num
