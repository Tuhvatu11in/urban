from django.shortcuts import render
from django.views.generic import TemplateView

def main(request):
  return render(request, 'fourth_task/main.html')

def shop(request):
  context = {'games' : ["Atomic Heart", "Cyberpunk 2077"]}
  return render(request, 'fourth_task/shop.html', context)

def bill(request):
  return render(request, 'fourth_task/bill.html')