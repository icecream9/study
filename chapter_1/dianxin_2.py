# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    n = int(raw_input())
    line = raw_input()
    li = line.split(" ")
    li = sorted(li, reverse=True)
    lii = []
    for it in li:
        lii.append(int(it))
    num_1 = lii[0]
    num_2 = lii[1]
    n_1 = 1
    n_2 = 1
    for i in range(2, len(lii)):
        if num_1 > num_2:
            if n_2 < n / 2:
                n_2 += 1
                num_2 += lii[i]
            else:
                n_1 += 1
                num_1 += lii[i]
        else:
            if n_1 < n / 2:
                n_1 += 1
                num_1 += lii[i]
            else:
                n_2 += 1
                num_2 += lii[i]
    if num_1 >= num_2:
        print num_1 - num_2
    else:
        print num_2 - num_1
