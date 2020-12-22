n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[-1]
second = arr[-2]

patten_sum = first * k + second
patten_size = k + 1
patten_iter = int(m / patten_size)

result = patten_sum * patten_iter + first * m % patten_size

print(result)


"""
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

parr.sort()

sum = 0
for i in range(m):
    if i % k == k-1: 
        sum += arr[-2]
    else:
        sum += arr[-1]

print(sum)
"""