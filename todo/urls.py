from django.urls import path
from . import views

app_name='todo'
urlpatterns = [
    path('', views.todo_list, name='list'),
    path('create/', views.todo_create, name='create'),
    path('<pk>/', views.todo_detail, name='detail'),
    path('<pk>/update/', views.UpdateView.as_view(), name='update'),
]
