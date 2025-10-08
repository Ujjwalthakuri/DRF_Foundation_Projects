
from django.contrib import admin
from django.urls import path, include
from todoApp import views
from rest_framework.routers import DefaultRouter
route = DefaultRouter()

route.register('todo', views.todoView, basename='totoapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
