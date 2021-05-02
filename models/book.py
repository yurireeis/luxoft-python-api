class Book():
    def __init__(self, data):
        info = data.get('volumeInfo')
        self.title=data.get('title')
        self.authors=info.get('authors')
        self.type='book'


    def json(self):
        return dict(title=self.title,authors=self.authors,type=self.type)
