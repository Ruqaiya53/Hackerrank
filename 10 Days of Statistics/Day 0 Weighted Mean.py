# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
elements = list(map(int, input().split()))
weights = list(map(int, input().split()))

mw_numerator = 0
mw_denomerator = 0
for i in range(0,size):
    mw_numerator +=elements[i]*weights[i]
    mw_denomerator +=weights[i]

mw = round(mw_numerator/mw_denomerator,1)

print(mw)
