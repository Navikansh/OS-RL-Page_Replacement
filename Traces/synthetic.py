import random

def generate_trace(length=1000, working_set=10):
    trace = []
    for _ in range(length):
        if random.random() < 0.8:
            trace.append(random.randint(0, working_set))
        else:
            trace.append(random.randint(0, working_set * 5))
    return trace
