from django.test import TestCase, Client
from django.urls import reverse
from ..models import Book, Author, Publisher
from django.core.files.uploadedfile import SimpleUploadedFile
import json


class BookListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('book_list')

    def test_view_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_list.html')


class ImportBooksViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('import_books')

    def test_import_books_post(self):
        json_data = json.dumps({
            "libri": [
                    {
                        "titolo": "Il Signore degli Anelli",
                        "autore": 1,
                        "editore": 1,
                        "anno edizione": "1954"
                    },
                ],
                "autori": [
                    {
                        "id": 1,
                        "nome": "J.R.R.",
                        "cognome": "Tolkien"
                    },
                ],
                "editori": [
                    {
                        "id": 1,
                        "ragione sociale": "Editor",
                        "indirizzo": "Via Editore 123"
                    },
                ]
        })
        json_file = SimpleUploadedFile(
            "books.json",
            json_data.encode(),
            content_type="application/json"
            )
        response = self.client.post(self.url, {'json_file': json_file})
        self.assertEqual(response.status_code, 302)


class BookListAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('api_book_list')
        self.author = Author.objects.create(
            first_name="Test Name",
            last_name="Test Lastame"
            )
        self.publisher = Publisher.objects.create(
            name="Test Editor",
            address="Via test 123",
            phone="123456789"
            )
        self.book = Book.objects.create(
            title="Test Book",
            publisher=self.publisher,
            year=2025
            )
        self.book.author.add(self.author)

    def test_api_list_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class BookCreateAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('api_book_create')
        self.author = Author.objects.create(
            first_name="Test Name",
            last_name="Test Lastame"
            )
        self.publisher = Publisher.objects.create(
            name="Test Editor",
            address="Via test 123",
            phone="123456789"
            )

    def test_api_create_book(self):
        data = {
            "title": "New Book",
            "author": [self.author.id],
            "publisher": self.publisher.id,
            "year": 2025
        }
        response = self.client.post(
            self.url,
            data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)
