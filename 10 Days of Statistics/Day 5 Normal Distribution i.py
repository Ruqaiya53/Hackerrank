# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def normal_dist(case,mean,std):
    z=(case-mean)/(std*(2**0.5))
    error=math.erf(z)
    return (1+error)*0.5

mean=20
std=2
case1=19.5
result1=normal_dist(case1, mean, std) 
print("{:.3f}".format(result1))
case2=20
result2=normal_dist(case2, mean, std)
case3=22
result3=normal_dist(case3, mean, std)
x=result3-result2
print("{:.3f}".format(x))
