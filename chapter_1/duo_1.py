# _*_ coding: utf-8 _*_


def main():
    line_1 = raw_input()
    k = int(line_1.split(" ")[0])
    n = int(line_1.split(" ")[1])
    m = int(line_1.split(" ")[2])
    array = []
    t_1 = []
    for i in range(0,n):
        line_t = raw_input()
        array.append([int(value.replace("\n", '')) for value in line_t.split(" ")])
        t_1.append(int(value.replace("\n", '')) for value in line_t.split(" "))
    # print array
    a_i = 0
    a_j = 1
    b_i = 1
    b_j = 0



if __name__ == "__main__":
    main()
