import json
from .models import Book, Author, Publisher
from django.core.exceptions import ObjectDoesNotExist

def import_books_from_json(data):
    for author_data in data.get('autori', []):
        Author.objects.update_or_create(
            id=author_data['id'],
            defaults={
                'first_name': author_data['nome'],
                'last_name': author_data['cognome']
            }
        )

    for publisher_data in data.get('editori', []):
        Publisher.objects.update_or_create(
            id=publisher_data['id'],
            defaults={
                'name': publisher_data['ragione sociale'],
                'address': publisher_data['indirizzo'],
                'phone': publisher_data.get('telefono', '')
            }
        )

    for book_data in data.get('libri', []):
        try:
            publisher = Publisher.objects.get(id=book_data['editore'])
            book, created = Book.objects.update_or_create(
                title=book_data['titolo'],
                publisher=publisher,
                year=book_data['anno edizione']
            )
            author_id = book_data.get('autore', '')
            authors = Author.objects.filter(id=author_id)
            book.author.set(authors)
        except ObjectDoesNotExist:
            print(f"Error importing books")
            continue
