class Book():
    def __init__(self, _id, data):
        info=data.get('volumeInfo')
        self.id=_id
        self.title=info.get('title')
        self.authors=info.get('authors')
        self.type='book'


    def json(self):
        return dict(id=self.id,title=self.title,authors=self.authors,type=self.type)
