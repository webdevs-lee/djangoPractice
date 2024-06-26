from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from foods.models import Menu

# Create your views here.
def index(request):
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context["date"] = today
    context["menus"] = menus
    
    return render(request, 'foods/index.html', context=context)

def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context['menu'] = menu
    # if food == "chicken":
    #     context["name"] = "코딩에 빠진 닭"
    #     context["description"] = "주머니가 가벼운 당신의 마음까지 생각한 가격!"
    #     context["price"] = 10000
    #     context["img_path"] = "foods/images/chicken.jpg"
    # else:
    #     raise Http404("이런 음식은 없음.")
    return render(request, 'foods/detail.html', context=context)