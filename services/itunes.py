from providers.http import HttpClient
from models.album import Album
from os import getenv


class ITunesService:
    def __init__(self):
        self.url = getenv('ITUNES_URL', 'https://itunes.apple.com')
        self.client = HttpClient()


    def get_albums(self, term, limit=5):
        current_url = self.url+'/search?'+'term='+term+'&limit='+str(limit)
        data = self.client.request('GET', current_url)
        results = data.get('results')
        if not results: return results
        return [Album(data).json() for data in results]
