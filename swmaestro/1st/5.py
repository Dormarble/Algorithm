import sys

input = sys.stdin.readline
def main():
    N = int(input())

    scores = []

    max_time = 0
    for _ in range(N*N):
        row = list(map(int, input().split()))
        s = row[0]
        times = row[2:]
        max_time = max(max_time, max(times))
        scores.append((s, times))

    scores.sort(reverse=True)


    time = [0]*(max_time + 1)
    for v, score in scores:
        for s in score:
            if time[s] == 0:
                time[s] = v

    print(sum(time))

if __name__=="__main__":
    main()