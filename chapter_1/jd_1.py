# _*_ coding: utf-8 _*_
"""笔试后才做出结果，也不知有多少的正确率
教训：缕青丝哭，不要在小地方出错而全盘结束"""


def main(list_1):
    if list_1.__len__() == 0:
        return 1
    sta = ["("]
    num = 0
    list_2 = "("
    print sta
    for i in range(1, len(list_1)):
        list_2 = list_2 + list_1[i]
        if list_1[i] == "(":
            num = 0
            sta.append("(")
            print sta
        else:
            sta.pop()
            print sta
            num += 1
            if sta.__len__() == 0:
                print "----,", num
                list_2 = list_2[1:-1]
                if i == len(list_1) - 1:
                    print "list", list_2

                    return num * main(list(list_2))
                else:
                    for j in range(i + 1, len(list_1)):
                        list_2 = list_2 + list_1[j]
                    num_1 = main(list(list_2))
                    print "list", list_2
                    return num * num_1
    return 1

if __name__ == '__main__':
    line = raw_input()
    list_1 = list(line)
    print main(list_1)
