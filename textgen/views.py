from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .model import TextGenModel
from .serializers import TextGenContextSerializer, TextGenRespSerializer
from .models import TextGenContext, TextGenResp
from .utils import filter_txt

class TextGenView(APIView):
    
    def get(self, request, *args, **kwargs):

        context = self.request.GET.get("context") # get input
        context = context[0:99] # limit 100 characters

        if TextGenContext.objects.filter(context=context).exists():
            gen_text = TextGenResp.objects.filter(context__context=context)
            serializer = TextGenRespSerializer(gen_text, many=True)
            result = {"response": serializer.data}
            return Response(result, status=status.HTTP_200_OK)
        
        context_serializer = TextGenContextSerializer(data=self.request.GET)
        if context_serializer.is_valid():
            context_serializer.save()

        textGenModel = TextGenModel(inp_context = context)
        gen_text, model_type = textGenModel.textGenBeamModel() # output
        
        filter_gen_text = filter_txt(data=gen_text)
        model_context = TextGenContext.objects.get(context=context)
        data = [{
                    "context": model_context.id,
                    "gen_text": filter_gen_text, 
                    "model_type": model_type
                }]
        print(f"Data >>> {data}")

        resp_serializer = TextGenRespSerializer(data=data, many=True)
        if resp_serializer.is_valid():
            resp_serializer.save()
            result = {"response": resp_serializer.data}
            return Response(result, status=status.HTTP_200_OK)
        
        return Response(context_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


