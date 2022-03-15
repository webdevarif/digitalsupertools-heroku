from django.urls import path
from .views import *

app_name="sites"

urlpatterns = [
    path('list', WebsiteList.as_view()),
    path('<slug:slug>', WebsiteDetail.as_view()),
    path('list/<str:username>', WebsiteUserList.as_view()),

    # Books
    path('books', BookList.as_view()),
    path('books/<slug:slug>', WebsiteBookList.as_view()),
    path('book-detail/<slug:slug>', BookDetail.as_view()),
]


