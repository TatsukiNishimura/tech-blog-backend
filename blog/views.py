from django.shortcuts import render
from rest_framework import viewsets

from blog.models import Blog
from blog.serializer import (BlogCreateSerializer, BlogListSerializer,
                             BlogRetrieveSerializer, BlogUpdateSerializer)


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        print(self.action)
        if self.action == "list":
            return BlogListSerializer
        elif self.action == 'create':
            return BlogCreateSerializer
        elif self.action == 'retrieve':
            return BlogRetrieveSerializer
        elif self.action in ['update', 'partial_update']:
            return BlogUpdateSerializer

        return super().get_serializer_class()
