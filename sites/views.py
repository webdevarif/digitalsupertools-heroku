from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from .models import *
from .serializers import *
from core.pagination import *
from rest_framework import status


from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from rest_framework_api_key.permissions import HasAPIKey  

# Website List
class WebsiteList(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

# Website List Per User
class WebsiteUserList(generics.ListCreateAPIView):
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

    def get(self, request, username, format=None):
        queryset = Website.objects.filter(user__username=username)
        serializers_data = WebsiteSerializer(queryset, many=True).data
        return Response(serializers_data)

# Book List
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination


# Book List
class SiteBookList(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )