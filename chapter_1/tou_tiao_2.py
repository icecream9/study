# _*_ coding: utf-8 _*_


def main(li, ll):
    num = 0
    for j in range(ll[0]-1, ll[1]):
        if ll[2] == li[j]:
            num += 1
    print num
    return

if __name__ == '__main__':
    n = int(raw_input())
    line_1 = raw_input()
    li_1 = [int(float(value)) for value in line_1.split(" ")]
    q = int(raw_input())
    for i in range(0,q):
        line_2 = raw_input()
        li_2 = [int(float(value)) for value in line_2.split(" ")]
        main(li_1,li_2)
