from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from django.http import JsonResponse
import random
import os
from Rasputin_TV.settings import BASE_DIR
import json
# Create your views here.

def get_shoppify(request):
    r = requests.get('https://f8a9fae48614bc8a75fdf30af0c32c73:7851e1da8a2c98c2ef8ea4dc770c4dc4@usedrecord.myshopify.com/admin/products.json')
    data = r.json()
    # print data
    # print type(data)

    strip_product = data['products']
    items_tuples = []
    for i in strip_product:
        # print i['title']
        # print i['image']['src']
        # print i['variants'][0]['price']
        items_tuples.append((i['title'], i['image']['src'], i['variants'][0]['price']))

    # for n in items_tuples:
    #     print n


    # for i in range(len(data['products'])):
    #     title = data['products'][i]['title']
    #     image = data['products'][0]['image']
    #     image = image['src']
    #     price = data['products'][0]['variants'][0]['price']
    #     items.append({"title": title, "image": image, "price": price})
    #
    #
    # for i in items:
    #     print i
    # print items
    # json_items = json.dumps(items)
    # # print json_items
    # print json_items
    item = random.choice(items_tuples)
    print item
    single_item_dict = {}
    single_item_dict["title"] = item[0]
    single_item_dict["image"] = item[1]
    single_item_dict["price"] = item[2]
    print single_item_dict
    # json_output = json.dumps(single_item_dict)
    # print json_output


    return JsonResponse(single_item_dict, safe=False)
def display(request):
    return render(request, "grab_content.html")