from django.urls import path
from .views import *

app_name="sites"

urlpatterns = [
    # Dog Age Calculator
    path('dog-age-calculator', DogAgeCalculatorList.as_view()),
    path('dog-age-calculator/years', DogAgeCalculatorYearList.as_view()),
    path('dog-age-calculator/sizes', DogAgeCalculatorSizeList.as_view()),

    
    # path('<slug:slug>', WebsiteDetail.as_view()),
    # path('list/<str:username>', WebsiteUserList.as_view()),

    # # Books Lists
    # path('books', BookList.as_view()),
    # path('books/<slug:slug>', WebsiteBookList.as_view()),
    # path('book-detail/<slug:slug>', BookDetail.as_view()),
    # path('book-page/<slug:slug>', BookPageDetail.as_view()),
]


