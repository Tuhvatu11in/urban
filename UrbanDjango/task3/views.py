from django.shortcuts import render
from django.views.generic import TemplateView

def main(request):
  return render(request, 'third_task/main.html')

def shop(request):
  return render(request, 'third_task/shop.html')

def bill(request):
  return render(request, 'third_task/bill.html')

