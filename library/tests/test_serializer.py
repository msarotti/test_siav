from django.test import TestCase
from ..models import Book, Author, Publisher
from ..serializers import AuthorSerializer, PublisherSerializer, BookSerializer


class AuthorSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Test Name",
            last_name="Test Name"
            )
        self.serializer = AuthorSerializer(instance=self.author)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'first_name', 'last_name'])

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['first_name'], "Test Name")
        self.assertEqual(data['last_name'], "Test Name")


class PublisherSerializerTest(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(
            name="Test Editor",
            address="Via test 123",
            phone="123456789"
            )
        self.serializer = PublisherSerializer(instance=self.publisher)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'name', 'address', 'phone'])

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], "Test Editor")
        self.assertEqual(data['address'], "Via test 123")
        self.assertEqual(data['phone'], "123456789")


class BookSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Test Name",
            last_name="Test Name"
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
        self.serializer = BookSerializer(instance=self.book)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['id', 'title', 'author', 'publisher', 'year']
        )

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], "Test Book")
        self.assertEqual(
            [str(author) for author in self.book.author.all()],
            ["Test Name Test Name"]
        )
        self.assertEqual(data['publisher'], self.publisher.id)
        self.assertEqual(data['year'], 2025)

    def test_invalid_data(self):
        invalid_data = {
            'title': '',
            'author': None,
            'publisher': None,
            'year': 'invalid'
        }
        serializer = BookSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
        self.assertIn('author', serializer.errors)
        self.assertIn('publisher', serializer.errors)
        self.assertIn('year', serializer.errors)
