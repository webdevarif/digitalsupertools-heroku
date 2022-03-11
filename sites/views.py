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

# Email Verify List
class WebsiteList(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination
