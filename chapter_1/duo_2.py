# _*_ coding: utf-8 _*_


def get_p(a):
    color = []
    d = []
    for i in range(0, 4):
        color.append(0)

    for i in range(0, 13):
        d.append(0)

    for it in a:
        if it[:1] == "S":
            color[0] += 1
        elif it[:1] == "H":
            color[1] += 1
        elif it[:1] == "C":
            color[2] += 1
        elif it[:1] == "D":
            color[3] += 1

        if it[1:] == "2":
            d[0] += 1
        elif it[1:] == "3":
            d[1] += 1
        elif it[1:] == "4":
            d[2] += 1
        elif it[1:] == "5":
            d[3] += 1
        elif it[1:] == "6":
            d[4] += 1
        elif it[1:] == "7":
            d[5] += 1
        elif it[1:] == "8":
            d[6] += 1
        elif it[1:] == "9":
            d[7] += 1
        elif it[1:] == "10":
            d[8] += 1
        elif it[1:] == "J":
            d[9] += 1
        elif it[1:] == "Q":
            d[10] += 1
        elif it[1:] == "K":
            d[11] += 1
        elif it[1:] == "A":
            d[12] += 1

    flush = 0
    for c in color:
        if c > 4:
            flush = 1

    d_max = sorted(d[:])[12]
    d_max_1 = sorted(d[:])[11]
    sun = 0
    j = 0
    i = 0
    while j < 13 and i < 13:
        if d[i] == 1:
            if j == 12:
                break
            j += 1
            if d[j] == 1:
                sun = j - i
            else:
                i = j + 1
                j = i
        else:
            i += 1
            j = i

    if d[0] == d[1] == d[2] == d[3] == d[12] == 1:
        sun = 4

    if d_max == 1 and sun < 4 and flush == 0:
        print "High Card"
        return
    elif d_max == 2 and d_max_1 == 1 and sun < 4 and flush == 0:
        print "One Pair"
        return
    elif d_max == 2 and d_max_1 == 2 and sun < 4 and flush == 0:
        print "Two Pair"
        return
    elif d_max == 3 and d_max_1 == 1 and sun < 4 and flush == 0:
        print "Three Pairs"
        return
    elif d_max < 4 and sun > 3 and flush == 0:
        print "Straight"
        return
    elif d_max == 3 and d_max_1 > 1:
        print "Full House"
        return
    elif flush == 1 and sun < 4:
        print "同花"
        return
    elif d_max == 4:
        print "四条"
        return
    else:
        if d[12] == d[11] == d[10] == d[9] == d[8] == 1 and 1 == 1:
            print "皇家童话混"
            return
        else:
            print "tonghuashun"
            return


def main():
    n = int(raw_input().replace("\n", ''))
    array = []
    for i in range(0, n):
        line_t = raw_input()
        array.append([value.replace("\n", '') for value in line_t.split(" ")])
    for i in range(0, n):
        get_p(array[i])


if __name__ == "__main__":
    main()
