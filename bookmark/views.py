from django.shortcuts import render

# Create your views here.

# 제너릭 뷰 : 웹 프로그래밍 많이 사용하는 기능을 미리 만들어 둔 형태
# 제너릭 뷰를 사용하고 싶다면 크래스형 뷰를 사용합니다.


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView


from .models import Bookmark


class BookmarkList(ListView):
    model = Bookmark
    template_name = 'bookmark/list.html'

    # html 페이지로 db의 model 을 넘길때
    #   여러가지 넘길때 object_list 로 넘어감
    #   단독으로 넘길때 object


class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = 'bookmark/detail.html'
    fields = ['site_name', 'url']


class BookmarkUpdate(UpdateView):
    model = Bookmark
    template_name = 'bookmark/update.html'
    success_url = '/'
    fields = ['site_name', 'url']


class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name = 'bookmark/delete.html'
    success_url = '/'


class BookmarkCreate(CreateView):
    model = Bookmark
    template_name = 'bookmark/create.html'
    fields = ['site_name', 'url']
    success_url = '/'
