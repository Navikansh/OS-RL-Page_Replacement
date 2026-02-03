import time

class FeatureTracker:
    def __init__(self):
        self.last_access = {}
        self.freq = {}
        self.insert_time = {}
        self.t = 0

    def on_access(self, page):
        self.t += 1
        self.last_access[page] = self.t
        self.freq[page] = self.freq.get(page, 0) + 1

    def on_insert(self, page):
        self.insert_time[page] = self.t

    def on_evict(self, page):
        self.last_access.pop(page, None)
        self.freq.pop(page, None)
        self.insert_time.pop(page, None)

    def features(self, page):
        return {
            "recency": self.t - self.last_access.get(page, self.t),
            "frequency": self.freq.get(page, 0),
            "age": self.t - self.insert_time.get(page, self.t)
        }
