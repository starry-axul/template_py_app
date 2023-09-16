from rest_framework import serializers
from templates.models import Template

class TemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Template  
        exclude = ['is_removed', 'created', 'modified']