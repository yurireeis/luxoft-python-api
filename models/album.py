from re import split


class Album():
    def __init__(self, _id, data):
        self.id=_id
        self.title=data.get('collectionName')
        self.authors=self.get_authors(data.get('artistName'))
        self.type='album'

    def get_authors(self, text):
        authors = split(', |_|-|!|&', text)
        return [author.strip() for author in authors]

    def json(self):
        return dict(id=self.id,title=self.title,authors=self.authors,type=self.type)
