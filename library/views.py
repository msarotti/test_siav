from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .forms import ImportJSONForm
from django.contrib import messages
import json
from library.utils import import_books_from_json


class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    ordering = ['title']


class ImportBooksView(FormView):
    template_name = 'library/import_books.html'
    form_class = ImportJSONForm
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        json_file = self.request.FILES['json_file']
        data = json.load(json_file)

        import_books_from_json(data)

        messages.success(self.request, 'Books imported successfully')
        return super().form_valid(form)


class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
