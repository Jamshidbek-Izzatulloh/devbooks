from django.shortcuts import render
from rest_framework import generics
from .serializers import AuthorSerializer, BookCategorySerializer, BookSerializer
from .models import AuthorModel, BookCategoryModel, BookModel

# LC means List & Create
# RUD means Retrieve, Update, & Destroy (Read, Update & Delete)


#CRUD for Book
class LCBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class RUDBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


#CRUD for Author
class LCAuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

class RUDAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

#CRUD for Book Category

class LCBookCategoryView(generics.ListCreateAPIView):
    queryset = BookCategoryModel.objects.all()
    serializer_class = BookCategorySerializer

class RUDBookCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategoryModel.objects.all()
    serializer_class = BookCategorySerializer


    