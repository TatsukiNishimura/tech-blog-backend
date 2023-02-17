from django.utils import timezone
from rest_framework import serializers

from blog.models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "created_at", "updated_at")


class BlogRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "content", "title", "created_at", "updated_at")


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("title", "content")


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("title", "content")

    def update(self, instance, validated_data):
        instance.updated_at = timezone.now()
        return super().update(instance, validated_data)
