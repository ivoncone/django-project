from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
from books.models import Book, Author
from books.serializers import AuthorSerializer, BookSerializer



class ListAuthorsAPIView(APIView):
	permissions_classes = (AllowAny,)

	def get(self, request):
		author_list = Author.objects.filter(status=True)
		serializer = AuthorSerializer(author_list, many=True)
		return Response(serializer.data)

class ListBooksAPIView(APIView):
	permissions_classes = (AllowAny,)

	def get(self, request):
		books_list = Book.objects.filter(status=True)
		serializer = BookSerializer(books_list, many=True)
		return Response(serializer.data)

class CreateAuthorAPIView(APIView):
	permissions_classes = (AllowAny,)

	def post(self, request):
		data = request.data
		serializer = AuthorSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBookAPIView(APIView):
	permissions_classes = (AllowAny, )

	def post(self, request):
		serializer = BookSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveAuthorAPIView(APIView):
	permissions_classes = (AllowAny,)

	def get(self, request, author_id):
		author_obj = get_object_or_404(Author, pk=author_id)
		serializer = AuthorSerializer(author_obj)
		return Response(serializer.data)

	def put(self, request, author_id):
		author_obj = get_object_or_404(Author, pk=author_id)
		serializer = AuthorSerializer(data=request.data)
		serializer = AuthorSerializer(instance=author_obj, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_OK)

	def delete(self, request, author_id):
		author_obj = get_object_or_404(Author, pk=author_id)
		author_obj.status = False
		author_obj.save()
		return Response({"Author has been deleted"}, status=status.HTTP_204_NO_CONTENT)

class RetrieveBookAPIView(APIView):
	permissions_classes = (AllowAny,)

	def get(self, request, book_id):
		book_obj = get_object_or_404(Book, pk=book_id)
		serializer = BookSerializer(book_obj)
		return Response(serializer.data)


	def put(self, request, book_id):
		book_obj = get_object_or_404(Book, pk=book_id)
		serializer = BookSerializer(instance=book_obj, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_OK)

	def delete(self, request, book_id):
		author_obj = get_object_or_404(id=book_id)
		book_obj.status = False
		book_obj.save()
		return Response({"Book has been deleted"}, status=status.HTTP_204_NO_CONTENT)




