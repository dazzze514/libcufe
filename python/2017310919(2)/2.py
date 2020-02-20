Fibonacci=[]
a=0
b=1
Fibonacci.append(b)
for n in range(2,21):
    cn=a+b
    Fibonacci.append(cn)
    a=b
    b=cn
print(Fibonacci)
    
    
