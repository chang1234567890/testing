# -*- coding: utf-8 -*-

"""附加题"""


def fun(data):

    lists = data.split(".")
    for i in range(len(lists)):
        lists[i] = int(lists[i])
        if len(lists) < 4:
            for i in range(4-len(lists)):
                lists.append(0)
    return lists


def fun2(version1, version2):
    version1 = fun(version1)
    version2 = fun(version2)
    for i in range(4):
        if version1[i] > version2[i]:
            return 1
        elif version1[i] < version2[i]:
            return -1
        elif i == 3:
            return 0


if __name__=="__main__":
    """
    输入: version1 = "0.1", version2 = "1.1"输出: -1
    输入: version1 = "1.0.1", version2 = "1"输出: 1
    输入: version1 = "7.5.2.4", version2 = "7.5.3"输出: -1
    输入：version1 = "1.01", version2 = "1.001"输出：0
    输入：version1 = "1.0", version2 = "1.0.0"输出：0
    """
    version1 = '0.1'
    version2 = '1.1'
    # version1 = '1.0.1'
    # version2 = '1'
    # version1 = "7.5.2.4"
    # version2 = "7.5.3"
    # version1 = "1.01"
    # version2 = "1.001"
    # version1 = "1.0"
    # version2 = "1.0.0"
    # version1 = '7.6.03.1'
    # version2 = '7.6.3.001'
    value = fun2(version1, version2)
    print(value)