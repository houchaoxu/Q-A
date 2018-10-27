from django.urls import path,re_path
from . import views

urlpatterns = [
    path('question/', views.qands, name="qands"),
    path('test/', views.test, name='test'),
]

