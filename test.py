#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'order' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH city
#  2. INTEGER company
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

from collections import deque

def order(city_nodes, city_from, city_to, company):
    visit = [False] * (city_nodes + 1)
    
    graph = [[] for _ in range(city_nodes + 1)]
    for a, b in zip(city_from, city_to):
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(city_nodes):
        graph[i].sort()
        
    result = []
    tmp = [company]
    visit[company] = True
    while tmp:
        q = deque(tmp)
        tmp = []
        while q:
            cur = q.popleft()
            
            for n in graph[cur]:
                if not visit[n]:
                    visit[n] = True
                    tmp.append(n)

        tmp.sort()
        for i in tmp:
            result.append(i)
            
    return result

    
print(order(5, [1, 1, 1, 2, 3], [2, 3, 5, 4, 5], 1))