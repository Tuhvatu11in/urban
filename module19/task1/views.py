from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

def main(request):
  return render(request, 'fourth_task/main.html')

def shop(request):
  context = {'games' : ["Atomic Heart", "Cyberpunk 2077"]}
  return render(request, 'fourth_task/shop.html', context)

def bill(request):
  return render(request, 'fourth_task/bill.html')

def sign_up_by_html(request):
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
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return redirect('/main/')


    return render(request, 'fifth_task/registration_page.html', {'users': users, 'info': info})
