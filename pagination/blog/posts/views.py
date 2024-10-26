from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post

def post_list(request):
  posts = Post.objects.all().order_by('-created_at')

  # Получаем количество элементов на странице из запроса
  items_per_page = request.GET.get('items_per_page', 10)
  paginator = Paginator(posts, items_per_page)

  page = request.GET.get('page')
  try:
    page_obj = paginator.get_page(page)
  except PageNotAnInteger:
    # Если страница не целое число, отображаем первую страницу
    page_obj = paginator.get_page(1)
  except EmptyPage:
    # Если номер страницы больше, чем общее количество страниц,
    # отображаем последнюю страницу
    page_obj = paginator.get_page(paginator.num_pages)

  context = {
    'page_obj': page_obj,
    'items_per_page': items_per_page, # Передаем количество элементов
  }
  return render(request, 'blog/post_list.html', context)
