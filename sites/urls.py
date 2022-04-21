from django.urls import path
from .views import *

app_name="sites"

urlpatterns = [
    # Website Lists
    path('list', WebsiteList.as_view()),
    path('<slug:slug>', WebsiteDetail.as_view()),
    path('list/<str:username>', WebsiteUserList.as_view()),

    # Books Lists
    path('books', BookList.as_view()),
    path('books/<slug:slug>', WebsiteBookList.as_view()),
    path('book-detail/<slug:slug>', BookDetail.as_view()),
    path('book-page/<slug:slug>', BookPageDetail.as_view()),
]


