from rest_framework import serializers
from .models import Template, Placeholder

class PlaceholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placeholder
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    placeholders = PlaceholderSerializer(many=True, read_only=True)

    class Meta:
        model = Template
        fields = '__all__'