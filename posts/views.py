from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .serializer import PostSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView




@api_view(['GET'])
def welcom(request):
  return Response({
     "message": "welcome to blog"
  })




@api_view(['GET'])
def post_detail(request, post_id):
   post = Post.objects.get(pk = post_id)
   comments = Comment.objects.filter(post = post)
   serializer = PostSerializer(post)
   return Response(serializer.data)



class Posts(APIView):

   @swagger_auto_schema(
         request_body=openapi.Schema(
         type=openapi.TYPE_OBJECT,
         properties={
             'name': openapi.Schema(type=openapi.TYPE_STRING, description='نام محصول'),
             'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='قیمت محصول'),
         }
        ),
      # request_body = PostSerializer,
         responses = {
            201 : 'create',
            400: 'bad request'
         }
   )
   def post (self, request):
      serializer = PostSerializer(data= request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
         "status": "ok"
         })
   
      return Response(serializer.errors, 400)
   
   def get(self, request):
      posts = Post.objects.all()
      serializer = PostSerializer(posts, many= True)
      return Response(serializer.data)



