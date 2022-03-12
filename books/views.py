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

class UpdateAuthorAPIView(APIView):
	permissions_classes = (AllowAny, )
	def put(self, request, author_id):
		author_obj = Author.objects.filter(id=author_id).first()
		serializer = AuthorSerializer(author_obj,data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

class UpdateBookAPIView(APIView):
	permissions_classes = (AllowAny, )
	def put(self, request, author_id):
		book_obj = Author.objects.filter(id=author_id).first()
		serializer = BookSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.update()
		return Response(serializer.data)

class DeleteAuthorAPIView(APIView):
	permissions_classes = (AllowAny, )
	def delete(self, request, author_id):
		author_obj = Author.objects.get(id=author_id)
		serializer = AuthorSerializer(data=request.data)
		author_obj.delete()
		return Response({"author has been deleted"})

class DeleteBookAPIView(APIView):
	permissions_classes = (AllowAny, )
	def delete(self, request, book_id):
		author_obj = Book.objects.get(id=book_id)
		serializer = AuthorSerializer(data=request.data)
		book_obj.delete()
		return Response({"book has been deleted"})




