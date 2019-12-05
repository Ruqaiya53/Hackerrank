# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

lamda = 2.5
k=5

result = ((lamda**k)*(math.exp(-lamda)))/(math.factorial(k))
print("{:.3f}".format(result))
