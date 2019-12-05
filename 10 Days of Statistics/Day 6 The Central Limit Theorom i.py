# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cmf(case,mean,std):
    z=(case-mean)/(std*(2**0.5))
    error=math.erf(z)
    return (1+error)*0.5

mean=100*2.4
std=10*2
case1=250
result1=cmf(case1, mean, std) 
print(round(result1,4))
