from django.test import TestCase
from rest_framework.exceptions import ValidationError
from library.models import Book, Author, Publisher
from ..serializers import BookSerializer


class TestBookSerializer(TestCase):

    def setUp(self):
        self.valid_author = Author.objects.create(
            first_name='John',
            last_name='Doe'
        )
        self.valid_author_id = self.valid_author.id
        self.valid_publisher = Publisher.objects.create(
            name='Test Publisher',
            address='123 Test St',
            phone='1234567890'
        )
        self.valid_publisher_id = self.valid_publisher.id

        self.valid_data = {
            'id': 1,
            'title': 'Test Book',
            'author': self.valid_author_id,
            'publisher': self.valid_publisher_id,
            'year': 2023
        }

        self.invalid_data_missing_fields = {
            'title': 'Test Book',
            'year': 2023
        }


    def test_valid_data_serialization(self):
        serializer = BookSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], self.valid_data['title'])
        self.assertEqual(serializer.validated_data['author'], self.valid_author)
        self.assertEqual(serializer.validated_data['publisher'], self.valid_publisher)
        self.assertEqual(serializer.validated_data['year'], self.valid_data['year'])

    def test_invalid_data_missing_fields(self):
        serializer = BookSerializer(data=self.invalid_data_missing_fields)
        self.assertFalse(serializer.is_valid())
        self.assertIn('author', serializer.errors)
        self.assertIn('publisher', serializer.errors)
