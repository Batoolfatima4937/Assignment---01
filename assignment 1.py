'''1. Temperature Classification:
Write a program that takes an input temperature from the user and classifies itas:'''



Temp=eval(input("Enter temperature"))
print(Temp)
if (Temp<0):
    print("Freezing")
elif (Temp>0 and Temp<=15):
    print("Cold")
elif (Temp>16 and Temp<=30):
    print("Moderate")
elif (Temp<=30):
    print("hot") 
else:
    print("its getting hot")
    

