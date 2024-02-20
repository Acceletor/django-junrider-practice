from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Food


# Create your views here.
def foods(request):
    all_foods = Food.objects.order_by('-is_premium')
    context = { 'foods': all_foods}
    return render(request, 'app_food/foods.html', context)

def food(request, food_id):
    each_food = None
    try:
        each_food = Food.objects.get(id=food_id)
    except: 
        print('can not find this index')
    context = {'food': each_food}
    return render(request, 'app_food/food.html', context)