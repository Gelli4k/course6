from rest_framework import serializers
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author_id', read_only=True)
    ad_id = serializers.IntegerField(source='ad_id', read_only=True)
    author_first_name = serializers.CharField(source='author_first_name', read_only=True)
    author_last_name = serializers.CharField(source='author_last_name', read_only=True)
    author_image = serializers.ImageField(source='author_image', read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'author_id', 'ad_id', 'author_last_name', 'author_last_name', 'author_image')



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'author')


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first.name', read_only=True)

    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'author_first_name')
