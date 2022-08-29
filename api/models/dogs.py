class Dogs():
    __table__ = 'anchorage_dog_names'
    columns = ['id', 'DogName', 'Count']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

