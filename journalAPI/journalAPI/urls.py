
from django.contrib import admin
from django.urls import path
from journalApp.views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('journals/', journalViewGetPost.as_view(), name='journal_list_create'),
    path('journals/<int:pk>/', journalViewRetrieveUpdateDelete.as_view(), name='journal_details'),
    path('journals/<int:pk>/restore/', restoreSoftDelete.as_view(), name='journal_restore'),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # path('authToken/', obtain_auth_token),
]
