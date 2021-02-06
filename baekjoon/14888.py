from copy import deepcopy
N = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

mi = 10e9
ma = -10e9

def f(r_a, r_op, x):
    global mi
    global ma

    if not r_a:
        mi = min(mi, x)
        ma = max(ma, x)
        return
    
    for i, op in enumerate(r_op):
        if op > 0:
            tmp_r_op = deepcopy(r_op)
            tmp_r_a = deepcopy(r_a)
            tmp_r_op[i] -= 1
            tmp_x = x
            if i == 0:
                tmp_x += tmp_r_a.pop(0)
            elif i == 1:
                tmp_x -= tmp_r_a.pop(0)
            elif i == 2:
                tmp_x *= tmp_r_a.pop(0)
            else:
                if tmp_x > 0:
                    tmp_x //= tmp_r_a.pop(0)
                else:
                    tmp_x = -tmp_x
                    tmp_x //= tmp_r_a.pop(0)
                    tmp_x = -tmp_x

            f(tmp_r_a, tmp_r_op, tmp_x)

init = a.pop(0)
f(a, op, init)

print(ma)
print(mi)