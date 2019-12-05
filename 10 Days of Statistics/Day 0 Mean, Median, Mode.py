from collections import Counter

n = int(input())
data = sorted([int(i) for i in input().split()])

Mean = sum(data)/n
Median = (data[n // 2] + data[-(n//2 + 1)]) / 2
Mode = sorted(sorted(Counter(data).items()), key = lambda x: x[1], reverse = True)[0][0]

print(Mean, Median, Mode, sep = '\n')
