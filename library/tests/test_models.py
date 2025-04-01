from django.test import TestCase
from ..models import Author, Publisher, Book


class AuthorModelTest(TestCase):
    def test_create_author(self):
        author = Author.objects.create(
            first_name="Test Name",
            last_name="Test Lastname"
            )
        self.assertEqual(str(author), "Test Name Test Lastname")


class PublisherModelTest(TestCase):
    def test_create_publisher(self):
        publisher = Publisher.objects.create(
            name="Test Editor",
            address="Via test 123",
            phone="123456789"
            )
        self.assertEqual(str(publisher), "Test Editor")


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Jane",
            last_name="Test Lastname"
            )
        self.publisher = Publisher.objects.create(
            name="Test Editor",
            address="Via test 123",
            phone="123456789"
            )
        self.book = Book.objects.create(
            title="Test Book",
            publisher=self.publisher, year=2025
            )
        self.book.author.add(self.author)

    def test_create_book(self):
        self.assertEqual(str(self.book), "Test Book")
        self.assertEqual(self.book.publisher.name, "Test Editor")
        self.assertEqual(self.book.year, 2025)
        self.assertEqual(list(self.book.author.all()), [self.author])
