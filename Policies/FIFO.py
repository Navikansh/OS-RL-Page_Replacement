from collections import deque
from Simulator.features import FeatureTracker

class FIFO():
    def __init__(self):
        self.queue = deque()
    
    def on_access(self, page):
        pass

    def on_insert(self, page):
        self.queue.append(page)

    def evict(self):
        return self.queue.popleft()
