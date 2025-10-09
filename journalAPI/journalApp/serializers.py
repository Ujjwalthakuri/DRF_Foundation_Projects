from .models import *
from rest_framework import serializers

class journalserializer(serializers.ModelSerializer):
    class Meta:
        model = journalModel
        fields = '__all__'
       