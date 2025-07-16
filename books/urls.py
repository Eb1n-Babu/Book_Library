from django.urls import path
from .views import BookList

urlpatterns = [
    path('',BookList,name='book_list'),
]
