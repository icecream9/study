# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    line_1= raw_input()
    n = int(line_1.split(" ")[0])
    k = int(line_1.split(" ")[1])
    line_2 = raw_input()
    like = [int(value) for value in line_2.split(" ")]
    temp = [like[i] for i in range(0,k)]
    sum = 0
    for itt in temp:
        sum = sum + itt
    res = [sum]
    temp.sort()
    for j in range(k,len(like)):
        if like[j] > temp[-1]:
            temp.remove(temp[-1])
            temp.append(like[j])
            temp.sort()
            sum = sum + like[j] - temp[-1]
            res.append(sum)
        else:
            res.append(sum)
    rst = ""
    for iii in res:
        rst = rst + str(iii) + " "
    print rst[:-1]
