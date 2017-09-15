# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    line_1= raw_input()
    n = int(line_1.split(" ")[0])
    m = int(line_1.split(" ")[1])
    c = int(line_1.split(" ")[2])
    li = []
    for i in range(0,n):
        list_t = raw_input().split(" ")
        if list_t[0] == "0":
            li.append([])
        else:
            li.append([int(list_t[j]) for j in range(1, len(list_t))])
    for i in range(0,c):
        wt = []
        for it in range(0, len(li)):
            if i in li[it]:
                wt.append(it)
        # ji suan wt shi fou hefa
        if wt.__len__() < 2:
            pass
        else:
            before = wt[0]
            for itt in range(0, len(wt)):
                pass

