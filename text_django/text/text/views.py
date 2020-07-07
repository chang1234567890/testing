# -*- coding: utf-8 -*-
import json
import operator

from django.http import HttpResponse, JsonResponse
from TestModel.models import Test
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def inserts(request):
    if request.method == 'POST':

        body = json.loads(str(request.body, encoding="utf8"))
    clients = body["client"]  # 客户
    stocks = int(body["stock"])   # 分数
    if 1 <= stocks <= 10000000:
        test1 = Test(client=clients, stock=stocks)
        test1.save()
        result = {"status": "成功"}
        return JsonResponse(result)
    else:
        result = {"status": "分数不在范围"}
        return JsonResponse(result)


@csrf_exempt
def get_ranking(request, num):
    ret = Test.objects.all().order_by("-add_date")[:int(num)]
    lists = []
    lists2 = []
    lists3 = []  # 保存区分客户端是否存在

    for i in ret:

        if i.client in lists3:

            # inde = lists3.index(i.client)
            # # lists3[inde][""]
            dicts = {

                "客户端": i.client,
                "分数": i.stock
            }
            lists2.append(dicts)
        else:
            lists3.append(i.client)
            dicts = {

                "客户端": i.client,
                "分数": i.stock
            }
            lists.append(dicts)
    lists = sorted(lists, key=lambda x : x['分数'], reverse=True)
    count = 0
    for j in lists:
        count += 1
        j["排名"] = count
        for i in lists2:
            if i["客户端"] == j["客户端"]:
                i["排名"] = count
    lis = lists+lists2

    return JsonResponse(lis, safe=False, content_type="application/json")

