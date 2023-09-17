from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TemplateSerializers
from .models import Template
from rest_framework import status
from django.http import Http404
from templates.service import TemplateService

class Templates(APIView):

    def __init__(self):
        self.service = TemplateService()

    def get(self, request, format=None, *args, **kwargs):

        
        data = self.service.get_templates()
        
        serializer = TemplateSerializers(data, many=True)
        
        res = {"status": "OK", "code": 200, "data": serializer.data}
        return Response(res)
    
    def post(self, request, format=None, *args, **kwargs):
        

        body = request.data
        data = self.service.create_template(body['title'], body['body'], body['placeholders'])
        print(data)
        serializer = TemplateSerializers(data, many=False)
        res = {"status": "OK", "code": 200, "data": serializer.data}
        return Response(res)
"""    
class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Post.objects.all()
        
    def post(self, request, format=None):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        """