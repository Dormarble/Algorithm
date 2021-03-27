import sys
import heapq

input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

sum = 0
while len(cards) != 1:
    s = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, s)
    sum += s

print(sum);




# import sys
# import heapq

# input = sys.stdin.readline

# N = int(input())
# q = []
# for _ in range(N):
#     heapq.heappush(q, int(input()))

# result = 0
# while len(q) != 1:
#     a = heapq.heappop(q)
#     b = heapq.heappop(q)
#     heapq.heappush(q, a+b)

#     result += a+b

# print(result)