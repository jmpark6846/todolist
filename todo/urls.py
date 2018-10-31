from django.urls import path
from . import views

app_name='todo'
urlpatterns = [
    path('', views.todo_list, name='list'),
    path('create/', views.todo_create, name='create'),
    path('<pk>/', views.todo_detail, name='detail'),
    path('<pk>/update/', views.TodoUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),
    path('<pk>/toggle/', views.todo_toggle_done, name='toggle_done'),
]
