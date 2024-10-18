from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'second_task/index2.html')

class index2(TemplateView):
    template_name = 'second_task/index.html'
