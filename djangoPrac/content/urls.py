from django.urls import path
from .views import Main, Modify, Post, delete, isGood, test  # views.py에서 import함

app_name='content'

urlpatterns=[
    path('main/', Main.as_view(),name='main'),
    path('main/post/', Post.as_view(),name='post'),
    path('main/post/<int:pk>', Modify.as_view(), name='modify'),   # pk로 변수이름 지정, views.py에서 받아옴
    path('main/delete/<int:pk>', delete, name='delete'),
    path('main/isGood/<int:pk>', isGood, name='isGood'),
    path('main/test', test, name='test'),
]