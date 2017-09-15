# _*_ coding: utf-8 _*_

def main(line):
    li = list(line)
    num = 0
    res = []
    for i in range(0,len(li)):
        if li[i] != "," and li[i] != " " and li[i] != ".":
            num += 1
        elif li[i] == ".":
            if num != 0:
                res.append(num)
            return res
        else:
            if num != 0:
                res.append(num)
                num = 0
    return res


if __name__ == '__main__':
    line = raw_input()
    ress = main(line)
    pp = ""
    for it in ress:
        pp = pp + str(it) + " "
    print pp[:-1]