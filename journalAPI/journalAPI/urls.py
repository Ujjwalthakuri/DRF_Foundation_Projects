
from django.contrib import admin
from django.urls import path
from journalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('journals/', journalViewGetPost.as_view(), name='journal_list_create'),
    path('journals/<int:pk>/', journalViewRetrieveUpdateDelete.as_view(), name='journal_details')
]
