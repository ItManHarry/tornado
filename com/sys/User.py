class User:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    @property
    def name(self):
        return self.name
    @property
    def code(self):
        return self.code