from rest_framework import serializers
from templates.models import Template


class TemplateSerializers(serializers.ModelSerializer):
    class Meta():
        model = Template
        fields = ('id', 'cluster', 'type', 'version', 'body', 'placeholders')


class RequestSerializer(serializers.Serializer):
    cluster = serializers.CharField(max_length=20)
    type = serializers.CharField(max_length=20)
    version = serializers.IntegerField(min_value=1)
    body = serializers.CharField(max_length=150)
    placeholders = serializers.ListField(child=serializers.CharField())
