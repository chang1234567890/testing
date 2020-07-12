# -*- coding: utf-8 -*-


def fun(data):
    lists = data.split(".")
    lis = list(map(str, (map(int, lists))))
    num = "".join(lis).ljust(4, '0')
    return int(num)


def fun2(version1, version2):
    version1 = fun(version1)
    version2 = fun(version2)

    if version1> version2:
        return 1
    elif version1 < version2:
        return -1
    else:
        return 0



if __name__=="__main__":
    """
    比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
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