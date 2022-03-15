from rest_framework import serializers
from accounts.serializers import *
from .models import *

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def to_representation(self, instance):
        # likes = Likes.objects.filter(post=instance.id)
        pages = Bookpage.objects.filter(book=instance.id)
        response = super().to_representation(instance)
        response['pages'] = BookpageSerializer(pages, many=True).data
        response['user'] = UserAccountSerializer(instance.user).data
        return response


class BookpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookpage
        fields = "__all__"
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserAccountSerializer(instance.user).data
        return response