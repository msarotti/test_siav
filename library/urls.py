from django.urls import path
from .views import (
    BookListAPI,
    BookCreateAPI,
    BookListView,
    ImportBooksView
    )


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('import/', ImportBooksView.as_view(), name='import_books'),
    path('api/books/', BookListAPI.as_view(), name='api_book_list'),
    path('api/books/create/', BookCreateAPI.as_view(), name='api_book_create'),
]
