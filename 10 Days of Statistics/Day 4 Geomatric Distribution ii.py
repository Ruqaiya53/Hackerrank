# Enter your code here. Read input from STDIN. Print output to STDOUT

n=5
p=1/3
result=0
for i in range(1,6):
    result+=(1-p)**(i-1)*p 
print("{:.3f}".format(result))
