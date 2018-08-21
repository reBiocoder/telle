from django.contrib import admin
from django.urls import path
from  . import   views


app_name="myblog"
urlpatterns = [
    path('index/', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('shownews/',views.shownews,name='shownews'),
    path('product/',views.product,name='product'),
    path('showproduct/',views.product,name='product'),

]

