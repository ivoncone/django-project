from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny

from books.serializers import AuthorSerializer

class AuthorViewSet(ModelViewSet):
	permissions_classes = (AllowAny, )
	class_serializer = AuthorSerializer

