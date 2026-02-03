from Simulator.features import FeatureTracker
def run_simulation(trace, cache, policy):
    hits, misses = 0, 0

    for page in trace:
        if cache.contains(page):
            hits += 1
            policy.on_access(page)
        else:
            misses += 1
            if cache.is_full():
                victim = policy.evict()
                for p in cache.pages:
                    print(p, FeatureTracker.features(p))
                cache.remove(victim)
                if hasattr(policy, "on_evict"):
                    policy.on_evict(victim)
            cache.add(page)
            policy.on_insert(page)

    return hits, misses
