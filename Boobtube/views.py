from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from django.http import JsonResponse
import random
import os
from Rasputin_TV.settings import BASE_DIR
# Create your views here.

def get_shoppify(request):
    r = requests.get('https://f8a9fae48614bc8a75fdf30af0c32c73:7851e1da8a2c98c2ef8ea4dc770c4dc4@usedrecord.myshopify.com/admin/products.json')
    data = r.json()
    items = []
    for i in range(len(data['products'])):
        title = data['products'][i]['title']
        image = data['products'][0]['image']
        image = image['src']
        price = data['products'][0]['variants'][0]['price']
        items.append({"title": title, "image": image, "price": price})


    # for i in items:
    #     print i
    # print items
    json_items = json.dumps(items)
    # print json_items
    print json_items
    item = random.choice(items)

    return JsonResponse(item)


def display(request):
    return render(request, "grab_content.html")