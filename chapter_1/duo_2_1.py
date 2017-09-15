# _*_ coding: utf-8 _*_


def get_p(a):
    d = []
    for i in range(0, 13):
        d.append([0, 0, 0, 0])
    for it in a:
        n_i = 0
        n_j = 0
        if it[0:1] == "H":
            n_j = 0
        elif it[0:1] == "S":
            n_j = 1
        elif it[0:1] == "C":
            n_j = 2
        elif it[0:1] == "D":
            n_j = 3

        if it[1:] == "2":
            n_i = 0
        elif it[1:] == "3":
            n_i = 1
        elif it[1:] == "4":
            n_i = 2
        elif it[1:] == "5":
            n_i = 3
        elif it[1:] == "6":
            n_i = 4
        elif it[1:] == "7":
            n_i = 5
        elif it[1:] == "8":
            n_i = 6
        elif it[1:] == "9":
            n_i = 7
        elif it[1:] == "10":
            n_i = 8
        elif it[1:] == "J":
            n_i = 9
        elif it[1:] == "Q":
            n_i = 10
        elif it[1:] == "K":
            n_i = 11
        elif it[1:] == "A":
            n_i = 12
        d[n_i][n_j] = 1
    # print d
    for i in range(0, 4):
        if d[8][i] == d[9][i] == d[10][i] == d[11][i] == d[12][i] == 1:
            print "皇家同花顺"


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
