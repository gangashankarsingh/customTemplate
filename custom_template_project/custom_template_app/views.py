from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class GetTemplate(APIView):
    def get(self, request):
        return Response({"status": "success", "data": "dummy response"}, status=status.HTTP_200_OK)
    
class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class PlaceholderViewSet(viewsets.ModelViewSet):
    queryset = Placeholder.objects.all()
    serializer_class = PlaceholderSerializer


