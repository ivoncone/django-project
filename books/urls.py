from django.urls import path 
from .views import views, modelview
from .views.modelview import AuthorViewSet

urlpatterns = [
	path('authors/list/', views.ListAuthorsAPIView.as_view()),
    path('authors/create/', views.CreateAuthorAPIView.as_view()),
    path('authors/<int:author_id>/', views.RetrieveAuthorAPIView.as_view()),

    path('book/list/', views.ListBooksAPIView.as_view()),
    path('book/create/', views.CreateBookAPIView.as_view()),
    path('book/<int:book_id>/', views.RetrieveBookAPIView.as_view()),

    path('viewset/author/list/', AuthorViewSet.as_view({'get':'list'})),
    path('viewset/author/create/', AuthorViewSet.as_view({'post':'create'})),
    path('viewset/author/<int:author_id>/', AuthorViewSet.as_view(
        {   
            'get':'retrieve', 
            'put':'partial_update', 
            'delete':'destroy'
        }
    )),
]