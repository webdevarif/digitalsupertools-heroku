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
class DogAgeCalculatorList(generics.ListCreateAPIView):
    queryset = DogAgeCalcualtor.objects.all()
    serializer_class = DogAgeCalculatorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination


# # Website Detail
# class DogAgeCalculatorDetails(generics.ListCreateAPIView):
    # queryset = DogAgeCalcualtor.objects.all()
#     serializer_class = DogAgeCalculatorSerializer
#     lookup_field = 'slug'
#     permission_classes = (permissions.AllowAny, )

    
# Website List Per User
class DogAgeCalculatorYearList(generics.ListCreateAPIView):
    queryset = DogAgeCalcualtorYear.objects.all()
    serializer_class = DogAgeCalculatorYearSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    # def get(self, request, username, format=None):
    #     queryset = Website.objects.filter(user__username=username)
    #     serializers_data = WebsiteSerializer(queryset, many=True).data
    #     return Response(serializers_data)

# Book List
class DogAgeCalculatorSizeList(generics.ListCreateAPIView):
    queryset = DogAgeCalcualtorSize.objects.all()
    serializer_class = DogAgeCalculatorSizeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
    

# Book List
# class WebsiteBookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]
#     pagination_class = StandardResultsSetPagination

#     # Get Books With Slug
#     def get_queryset(self):
#         slug = self.kwargs['slug']
#         return Book.objects.filter(website__slug=slug)

# # Book Detail
# class BookDetail(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'slug'
#     permission_classes = (permissions.AllowAny, )
    

# # Book Page Detail
# class BookPageDetail(generics.RetrieveAPIView):
#     queryset = Bookpage.objects.all()
#     serializer_class = WebsiteSerializer
#     lookup_field = 'slug'
#     permission_classes = (permissions.AllowAny, )
    