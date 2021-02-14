
from django.urls import path,include
from django.contrib import admin
from task1.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task1.urls', namespace='task1' ))
]
