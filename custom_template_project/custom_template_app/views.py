from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *
import re

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



class TemplateAndPlaceholdersView(APIView):
    def get(self, request):
        try:
            template_id = request.GET.get("template_id")
            template = Template.objects.get(pk=template_id)
            placeholders = Placeholder.objects.filter(template=template)
            template_data = TemplateSerializer(template).data
            placeholders_data = [placeholder.name for placeholder in placeholders]

            response_data = {
                "template": template_data,
                "placeholders": placeholders_data,
            }
            return Response(response_data)
        except Template.DoesNotExist:
            return Response({"error": "Template not found"}, status=status.HTTP_404_NOT_FOUND)
        

class TemplateAndPlaceholdersViewUpdated(APIView):
    def get(self, request):
        try:
            template_id = request.GET.get("template_id")
            template = Template.objects.get(pk=template_id)
            template_content = template.content
            resultset_list = []

            pattern = r'{{\d+}}'
            matches = re.findall(pattern, template_content)
            total_placeholder_count = len(matches)


            employee_set = list(Employee.objects.values_list('name','designation'))

            if  len(employee_set) > 0 and  len(employee_set[0]) == total_placeholder_count:
                temp_template_content = template_content
                for employee in employee_set:
                    employee = list(employee)
                    for match in matches:
                        temp_template_content =  re.sub(re.escape(match), employee.pop(0) , temp_template_content)
                    resultset_list.append(temp_template_content)
            response_data = {
                "status": "success",
                "template_list": resultset_list,
            }
            return Response(response_data)     

                    
            




        except Template.DoesNotExist:
            return Response({"error": "Template not found"}, status=status.HTTP_404_NOT_FOUND)


