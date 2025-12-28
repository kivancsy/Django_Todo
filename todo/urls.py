from django.urls import path, include

from todo import views

urlpatterns =[
    path('add-task/', views.add_task, name = 'add_task'),
    path('mark-as-done/<int:pk>/', views.mark_as_done, name = 'mark_as_done'),
    path('mark-as-undone/<int:pk>', views.mark_as_undone, name = 'mark_as_undone')
]