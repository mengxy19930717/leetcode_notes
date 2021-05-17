import pandas as pd
import heapq

def build_map(df, col_name):
    pass

if __name__ == '__main__':
    a = [1,3,6,4,2,5]
    heap = []
    for i in range(len(a)):
        heapq.heappush(heap, a[i])
    print(heap)
    heapq.heappop(heap)
    print(heap)
    heapq.heappush(heap, 3)
    print(heap)
    print(heapq.nlargest(1, heap))
