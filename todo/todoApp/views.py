from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class todoView(viewsets.ModelViewSet):
    queryset = todoModel.objects.all()
    serializer_class = todoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    # ordering_fields = ['title']
    ordering = ['title']
    
    def get_queryset(self):
        return todoModel.objects.filter(user = self.request.user)
    
    