A=int(input("enter the first number: "))
B=int(input("enter the second number: "))
if A>B:
    LCM=A
else:
    LCM=B
while(1):
    if((LCM%A==0) and (LCM%B==0)):
        print("LCM is: ", LCM)
        break
    LCM+=1
    
