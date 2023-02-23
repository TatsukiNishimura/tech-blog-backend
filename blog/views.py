from rest_framework import filters, viewsets

from blog.models import Blog
from blog.permissions import BlogAuthentication
from blog.serializer import (BlogCreateSerializer, BlogListSerializer,
                             BlogRetrieveSerializer, BlogUpdateSerializer)


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
    permission_classes = (BlogAuthentication, )
    filterset_fields = ['id']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        elif self.action == 'create':
            return BlogCreateSerializer
        elif self.action == 'retrieve':
            return BlogRetrieveSerializer
        elif self.action in ['update', 'partial_update']:
            return BlogUpdateSerializer
        return super().get_serializer_class()
