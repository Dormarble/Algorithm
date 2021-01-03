str_n = input()

size = len(str_n) // 2 

left_sum, right_sum = 0, 0
for i in str_n[:size]:
    left_sum += int(i)
for i in str_n[size:]:
    right_sum += int(i)

if right_sum == left_sum:
    print("LUCKY")
else:
    print("READY")