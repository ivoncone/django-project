from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
from books.models import Book, Author
from books.serializers import AuthorSerializer, BookSerializer

class RetrieveBooks(APIView):
	permissions_classes = (AllowAny,)

	def get(self, request):
		books_list = Book.objects.all()
		serializer = BookSerializer(books_list, many=True)
		return Response(serializer.data)

class RetrieveAuthors(APIView):
	permissions_classes = (AllowAny,)

	def get(self, request):
		author_list = Author.objects.all()
		serializer = AuthorSerializer(author_list, many=True)
		return Response(serializer.data)

class CreateAuthor(APIView):
	permissions_classes = (AllowAny,)

	def post(self, request):
		data = request.data
		serializer = AuthorSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)



class CreateBook(APIView):
	permissions_classes = (AllowAny, )

	def post(self, request):
		serializer = BookSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveAuthorAPIView(APIView):
	permissions_classes = (AllowAny,)
	def get(self, request, author_id):
		author_obj = Author.objects.get(id=author_id)
		serializer = AuthorSerializer(author_obj)
		return Response(serializer.data)

class RetrieveBookAPIView(APIView):
	permissions_classes = (AllowAny,)
	def get(self, request, book_id):
		book_obj = get_object_or_404(Book, pk=book_id)
		serializer = BookSerializer(book_obj)
		return Response(serializer.data)

