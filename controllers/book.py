from flask_restful import Resource, reqparse, inputs, abort
from services.google import GoogleBooksService

class BooksController(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('term', type=str, location='args', required=True)
        parser.add_argument('limit', type=int, location='args', required=False, default=5)
        args = parser.parse_args()

        try:
            return GoogleBooksService().get_books(args.term, args.limit), 200
        except Exception as e:
            return e, 400
