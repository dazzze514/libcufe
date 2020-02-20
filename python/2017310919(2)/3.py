d=[]
car_num=[]
for a in range(1,10):
    for b in range(0,10):
        if a!=b:
            c=1000*a+100*a+10*b+b
            d.append(c)
for e in d:
    for n in range(1,100):
        if e==n**2:
            car_num.append(e)
print(car_num)
            
