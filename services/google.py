from providers.http import HttpClient
from models.book import Book
from os import getenv


class GoogleBooksService:
    def __init__(self):
        self.url = getenv('GOOGLE_BOOKS_URL', 'https://www.googleapis.com/books/v1')
        self.client = HttpClient()


    def get_books(self, term, limit=5):
        current_url = self.url+'/volumes?'+'q='+term+'&maxResults='+str(limit)
        data = self.client.request('GET', current_url)
        items = data.get('items')
        if not items: return items
        return [Book(data).json() for data in items]
