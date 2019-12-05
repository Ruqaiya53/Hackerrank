# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b1,b2, p, n = 0, 0, 12/100, 10
for i in range(3):
    b1 += bi_dist(i, n, p)  

for i in range(2,n+1):
    b2 += bi_dist(i, n, p)  
print("{:.3f}".format(b1))
print("{:.3f}".format(b2))
