# -*- coding: utf-8 -*-
import random
import json
import socket

from requests import request

"""测试接口脚本"""

ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))  # 本机ip地址
url = "http://%s:8002/" % ip  # 启动的url
count = 11  # 需要查询的个数


def inster():
    name = "客戶端"
    num = 1
    for i in range(0, 11):
        stock = random.randint(1, 10000000)
        if i == 5:  # 当是客户端5的时候再一次添加
            num = 0
        count = i+num
        datas = {
            "client": name+str(count),
            "stock": stock
        }
        data = json.dumps(datas)
        urls = url+"inserts/"
        req = request(method="POST", url=urls, data=data, timeout=20)
        print(req.json())


def get_data():
    urls = url+"get_ranking/11/"
    req = request(method="POST", url=urls, timeout=20)
    data = req.json()
    print("\t\t\t\t=====================================================")
    print("\t\t\t\t\t\t|排名|\t客户端|\t分数")
    for i in data:
        print("\t\t\t\t\t\t---------------------------")
        print("\t\t\t\t\t\t|%s\t  %s\t %s" % (i["排名"], i["客户端"], i["分数"]))


if __name__ == "__main__":
        inster()  # 添加数据
        get_data()  # 查询数据
