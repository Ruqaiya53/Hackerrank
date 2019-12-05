# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import mean
from statistics import stdev
import math

size = int(input())
items = list(map(int, input().split()))

mean_of_items = sum(items)/size

list_for_stdev = []
temp_stdev = 0
for i in range(size):
    temp_stdev = (items[i]-mean_of_items)**2
    list_for_stdev.append(temp_stdev)

stdev = math.sqrt(sum(list_for_stdev)/size)

print("{:.1f}".format(stdev))

