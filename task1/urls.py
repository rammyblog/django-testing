
from django.urls import path
from . import views

app_name = 'task1'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post>/', views.post_single, name='post_single'),
]