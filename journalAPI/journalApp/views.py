from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class journalViewGetPost(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = journalModel.objects.filter(is_deleted=False)
    serializer_class = journalserializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class journalViewRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = journalModel.objects.all()
    serializer_class = journalserializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return journalModel.objects.filter(user = self.request.user, is_deleted = False)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
       instance = self.get_object()
       instance.is_deleted = True
       instance.save()
       return Response ({'msg': 'journal soft delete successfully'})
      

class restoreSoftDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            jor = journalModel.objects.get(pk=pk, user=request.user, is_deleted=True)
            jor.is_deleted=False
            jor.save()
            return Response({'msg': 'journal restore'})
        except:
            return Response({'msg': 'journal not found or already activate'}, status=status.HTTP_404_NOT_FOUND)
