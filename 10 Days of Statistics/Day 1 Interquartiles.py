# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

size = int(input())

items = list(map(int, input().split()))
frq = list(map(int, input().split()))

final_list = []
for i in range(0,size):
    temp_item = items[i]
    for j in range(0,frq[i]):
        final_list.append(temp_item)

final_list = sorted(final_list)
size_final_list = len(final_list)

q1 = median(final_list[:size_final_list//2])
q3 = median(final_list[(size_final_list+1)//2:])

result = q3-q1
print("{:.1f}".format(result))

    
