class Registry:

    def __init__(self):
        self.links = []

    def add(self, link):
        self.links.append(link)

    def all(self):
        return self.links

    def find(self, code):

        for link in self.links:

            if link.code == code:
                return link

        return None
