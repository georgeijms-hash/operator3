print("=======================================")
print("    welcome to rider builder ")
print("=======================================")
print()
print("step 1-pick your vechil")
print("1-bike")
print("2-car")
choice=int(input("enter 1 or 2"))
print()
if choice==1:
    print("step2-pick your bike type")
    print("`1-soocty")
    print("2-mountain bike")
    print()
    bike_type=int(input("enter 1 or 2"))    
    if bike_type==1:
        print("you picked:scooty")
        print("top speed:80km/h")
        print("good for:city")
    else:
        print("you picked:mountain bike")
        print("top speed:40km/h")
        print("good for:adventure")
elif choice==2:
    print("step2-pick your car type")
    print("1-sadan")
    print("2-SUV")
    print()
    car_type=int(input("enter 1 or 2"))    
    if car_type==1:
        print("you picked:sadan")
        print("good for:city")
    else: 
        print("you picked:SUV") 
        print("good for:trips ")
else:
    print("choice invalid")         
         
     
             
             


  
