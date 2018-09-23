from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def one(request):
    return  render(request, r"one.html")

def two(request):

   # 用来存放向模板中传递的数据
   ct = dict()
   ct["name"] = "刘怡然"
   ct['name2'] = "李晓静"
   ct['name3'] = "张晓静"

   return  render(request, r"two.html", context=ct)


def three(request):
   ct = dict()

   ct["score"] = [99,87,23, 100,83, 87]
   return  render(request, r"three.html", context=ct)

def four(request):
   ct = dict()

   ct["name"] = "李晓静"
   return  render(request, r"four.html", context=ct)

def five_get(request):
   return render(request, 'five_get.html')

def five_post(request):
   print(request.POST)
   return render(request, 'one.html')
