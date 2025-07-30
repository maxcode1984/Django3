from django.urls import path
from .views import news_detail, news_list

urlpatterns = [
    path('news/', news_list, name='news'),
    path('news/<int:pk>/', news_detail, name='news_detail')
]