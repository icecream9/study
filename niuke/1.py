# _*_ coding: utf-8 _*_
"""在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。"""
"""start from the [length][0] to the first line"""


def main(array, target):
    i = 0
    j = len(array)
    while i < len(array[0]) and j >= 0:
        if array[j][i] > target:
            j -= 1
        elif array[j][i] < target:
            i += 1
        else:
            return True
    return False


if __name__ == "__main__":
    arr = []
    k = 3
    main(arr, k)
