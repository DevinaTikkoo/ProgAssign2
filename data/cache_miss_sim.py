import sys 
import heapq
import collections

#Global variables:
#Representation of infinity 
inf = float('inf')

def parse_input(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
        #First line contains the number of cache lines and the number of accesses
        #Place into map 
        k, m = map(int, lines[0].strip().split())
        #Memory request IDs; separator = whitespace 
        access_tokens = " ".join(lines[1:]).split()
        #Add ids to list of int
        r = [int(t) for t in access_tokens]

    if len(r) != m:
        raise ValueError(
            f"Expected {m} requests, but found {len(r)}."
        )

    if k < 1:
        raise ValueError("Cache capacity k must be >= 1.")

    return k, m, r

def FIFO_miss(k, r):
    cache = set()
    queue = collections.deque()
    count = 0

    for id in r:
        if id not in cache:
            count += 1
            if len(cache) < k:
                #No eviction needed, just add new entry  
                cache.add(id)
                queue.append(id)
            else:
                #Remove oldest entry from cache and queue, add new entry 
                evicted = queue.popleft()
                cache.remove(evicted)
                cache.add(id)
                queue.append(id)
    return count 


def LRU_miss(k, r):
    #Place least-recently used entry at front of queue 
    od = collections.OrderedDict()
    count = 0

    for id in r:
        if id in od:
            #Most-recently used, so move to end of queue
            od.move_to_end(id)
        else:
            count += 1
            if len(od) >= k:
            #Cache full, evict least-recently used entry (front of queue)
                od.popitem(last=False)
            #Add new entry to end of queue
            od[id] = None
    return count