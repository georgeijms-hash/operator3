print("marks")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
tot=m1+m2+m3+m4+m5
avg=int(tot/5)
validrange=range(0,101)
if avg not in validrange:
    print("invalid input")
elif avg in range(91,101):
    print("grade A1")
elif avg in range(81,91):
    print("grade A2")
elif avg in range(71,81):
    print("grade B1") 
elif avg in range(61,71):
    print("grade B2")  
elif avg in range(51,61):
    print("grade C1")     
else:
    print("fail")       