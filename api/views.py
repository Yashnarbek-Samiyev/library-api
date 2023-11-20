from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Book, LibUser, RentBook
from .serializers import BookSerializer, LibUserSerializer, RentBookSerializer
from rest_framework.response import Response


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LibUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


class RentBookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer
