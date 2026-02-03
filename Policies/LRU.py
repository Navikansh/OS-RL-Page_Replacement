from collections import OrderedDict

class LRU:
    def __init__(self):
        self.cache = OrderedDict()

    def on_access(self, page):
        if page in self.cache:
            self.cache.move_to_end(page)

    def on_insert(self, page):
        self.cache[page] = None

    def evict(self):
        return self.cache.popitem(last=False)[0]
