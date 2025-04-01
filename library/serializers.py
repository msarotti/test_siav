from rest_framework import serializers
from .models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'phone']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all()
        )
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all()
        )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'year']

    def to_internal_value(self, data):
        if isinstance(data.get('author'), int):
            data['author'] = [data['author']]
        return super().to_internal_value(data)
