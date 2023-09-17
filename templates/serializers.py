from rest_framework import serializers
from templates.models import Template

class TemplateSerializers(serializers.ModelSerializer):
    class Meta():
        model = Template  
        fields = ('id','title','body','placeholders')