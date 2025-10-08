from .models import *
from rest_framework import serializers
class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoModel
        fields = '__all__'
        read_only_fields = ['id','created_at', 'updated_at']