from flask import Flask
from flask_restful import Api
from controllers.book import BooksController
from controllers.album import AlbumsController
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(AlbumsController, '/albums', endpoint='albums')
api.add_resource(BooksController, '/books', endpoint='books')


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
