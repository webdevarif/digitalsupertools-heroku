from django.urls import path
from .views import *

app_name="sites"

urlpatterns = [
    path('list', WebsiteList.as_view()),
]


