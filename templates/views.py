from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from .responses import OK, BadRequest, endpoint
from .serializers import TemplateSerializers, RequestSerializer
from .models import Template
from rest_framework import status
from django.http import Http404
from templates.service import TemplateService

class Templates(APIView):

    def __init__(self):
        self.service = TemplateService()

    @endpoint
    def get(self, request, format=None, *args, **kwargs):
        cluster = request.GET.get("cluster")            
        type = request.GET.get("type")
        version = request.GET.get("version")

        serializer = TemplateSerializers(
            self.service.get_templates(cluster, type, version)
            , many=True)
    
        return OK(serializer.data)

        
    @endpoint
    def post(self, request, format=None, *args, **kwargs):
        
        serializer = RequestSerializer(data=request.data)

        if not serializer.is_valid():
            return BadRequest(serializer.errors)
        
        body = serializer.data

        response = TemplateSerializers(
            self.service.create_template(body['cluster'], body['type'], body['version'], body['body'], body['placeholders'])
            , many=False)
        return OK(response.data)
        
        
        


class Templates_Detail(APIView):

    def __init__(self):
        self.service = TemplateService()

    @endpoint
    def get(self, request,id, format=None):

        data = self.service.get_template(id)
        
        serializer = TemplateSerializers(data, many=False)
        
        return OK(serializer.data)
    


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