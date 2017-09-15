# _*_ coding: utf-8 _*_


def main(li, length):
    num_0 = 0
    num_1 = 0
    num_2 = 0
    for number in li:
        if number % 2 == 0:
            num_1 += 1
            if number % 4 == 0:
                num_2 += 1
        else:
            num_0 += 1
    num_1 = num_1 - num_2
    # print num_0, num_1, num_2
    if length % 2 == 0:
        if num_2 * 2 >= length:
            print "Yes"
            return
        else:
            # print "No"
            if num_0 <= num_2:
                print "Yes"
                return
            else:
                print "No"
                return

    else:
        if num_2 * 2 + 1 >= length:
            print "Yes"
            return
        else:
            if num_0 <= num_2:
                print "Yes"
                return
            else:
                print "No"
                return

            return


if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        length = int(raw_input())
        line = raw_input()
        list_t = [int(value) for value in line.split(" ")]
        main(list_t, length)
