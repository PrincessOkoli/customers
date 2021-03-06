from django.urls import path
from api import views

urlpatterns =[
    path('', views.index, name='index'),
    path('createtodo', views.createtodo, name='createtodo'),
    path('alltodos', views.alltodos, name='alltodos'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]