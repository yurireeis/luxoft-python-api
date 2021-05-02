from flask_restful import Resource, reqparse, inputs, abort
from services.itunes import ITunesService

class AlbumsController(Resource):
    def get(self):
        try:
            return ITunesService().get_albums('michael jackson'), 200
        except Exception as e:
            return e, 400
