
answer = 0


def dev(arr, result):
    global answer
    if len(arr) == 1:
        answer = max(answer, result)
        return
    
    n = len(arr) // 2
    dev(arr[:n], result+max(arr[n:]))
    dev(arr[n:], result+max(arr[:n]))

def main():
    N = int(input())
    arr = list(map(int, input().split()))

    dev(arr, 0)
    print(answer)


if __name__=="__main__":
    main()
