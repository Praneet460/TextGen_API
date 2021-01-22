from rest_framework import serializers
from .models import TextGenContext, TextGenResp

class TextGenContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextGenContext
        fields = '__all__'

class TextGenRespSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextGenResp
        fields = '__all__'