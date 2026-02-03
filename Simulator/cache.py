class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = set()

    def contains(self, page):
        return page in self.pages

    def add(self, page):
        self.pages.add(page)

    def remove(self, page):
        self.pages.remove(page)

    def is_full(self):
        return len(self.pages) >= self.capacity
