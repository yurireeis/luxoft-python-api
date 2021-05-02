from flask_restful import Resource, reqparse, inputs, abort
from services.google import GoogleBooksService

class BooksController(Resource):
    def get(self):
        try:
            return GoogleBooksService().get_books('michael jackson'), 200
        except Exception as e:
            return e, 400
