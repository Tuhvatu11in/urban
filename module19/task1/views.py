# Create your views here.
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Buyer, Game


def main(request):
    return render(request, 'fourth_task/main.html')


def shop(request):
    context = {"games": Game.objects.all()}
    return render(request, 'fourth_task/shop.html', context)


def bill(request):
    return render(request, 'fourth_task/bill.html')


users = []


def sign_up_by_html(request):
    if not request.user.is_authenticated:
        info = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username):
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return redirect('/main/')
            return render(request, 'fifth_task/registration_page.html', {'users': users, 'info': info})
    else:
         return redirect('/main/')

