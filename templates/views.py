from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TemplateSerializers
from .models import Template
from rest_framework import status
from django.http import Http404

class Templates(APIView):
    def get(self, request, format=None, *args, **kwargs):
        #print(help(request))
        data = {"status": "OK", "code": 200}
        #post = Template.objects.all()
        #serializer = TemplateSerializers(data, many=True)
        
        return Response(data)


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