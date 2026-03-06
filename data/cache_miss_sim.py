import sys 
import heapq
import collections

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

def FIFO(k, r):
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


def LRU(k, r):
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

def OPTFF(k, r):
    cache = set()
    count = 0
    #representation of infinity 
    inf = float('inf')

    for i, id in enumerate(r):
        if id not in cache:
            count += 1
            if len(cache) < k:
                #No eviction needed; add new entry 
                cache.add(id)
            else:
                #Cache full
                #Find cached entry with farthest next use/no future use
                farthest_next = -1
                evict_id = None
                for cached_id in cache:
                    try:
                        next = r.index(cached_id, i + 1)
                    except ValueError:
                        #If cached_id is not used again, treat as infinity
                        next = inf
                    if next > farthest_next:
                        farthest_next = next
                        evict_id = cached_id
                #evict entry; add new entry 
                cache.remove(evict_id)
                cache.add(id)
    return count


def main():
    if len(sys.argv) != 2:
        print("Usage: python cache_miss_sim.py <input_file>")
        return

    input_ = sys.argv[1]
    k, m, r = parse_input(input_)

    if len(r) != m:
        print(f"Error: Found {len(r)} requests, but expected {m} requests.")
        return

    print(f"FIFO  : {FIFO(k, r)}")
    print(f"LRU   : {LRU(k, r)}")
    print(f"OPTFF : {OPTFF(k, r)}")


if __name__ == "__main__":
    main()