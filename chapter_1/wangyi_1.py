# _*_ coding: utf-8 _*_


def main(n, l, li):
    global ret
    list_0 = []
    for i in range(0, n):
        if li[0][i] == 1:
            list_0.append(i)

    for i in range(0, n):
        pass
    pass

if __name__ == '__main__':
    ret = []
    line_1 = raw_input()
    n = int(line_1.split(" ")[0])
    l = int(line_1.split(" ")[1])
    line_2 = raw_input()
    list_1 = [int(value) for value in line_2.split(" ")]
    list_t = []
    for i in range(0, n):
        list_tt = []
        list_t.append(list_tt)
    for i in range(0, n-1):
        list_t[i+1].append(list_1[i])
        list_t[list_1[i]].append(i+1)
    print list_t
    main(n, l, list_t)
