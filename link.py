class Link:

    def __init__(self, title, url, code):
        self.title = title
        self.url = url
        self.code = code
        self.visits = 0

    def open(self):
        self.visits += 1
