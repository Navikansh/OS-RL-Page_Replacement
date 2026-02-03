from collections import defaultdict

class LFU:
    def __init__(self):
        self.freq = defaultdict(int)
        self.in_cache = set()

    def on_access(self, page):
        if page in self.in_cache:
            self.freq[page] += 1

    def on_insert(self, page):
        self.in_cache.add(page)
        self.freq[page] += 1

    def on_evict(self, page):
        self.in_cache.remove(page)
        del self.freq[page]

    def evict(self):
        # Choose LFU page among pages currently in cache
        return min(self.in_cache, key=lambda p: self.freq[p])
