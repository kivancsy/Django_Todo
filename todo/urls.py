from django.urls import path, include

from todo import views

urlpatterns =[
    path('add-task/', views.add_task, name = 'add_task'),
]