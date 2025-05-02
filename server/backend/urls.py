from django.contrib import admin
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/users$', views.users_list),
    re_path(r'^api/users/(?P<id>\d+)$', views.users_detail),  # Modified regex
]
