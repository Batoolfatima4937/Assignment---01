name=input("Enter student name")
maths=eval(input("Enter the Student maths num"))
physics=eval(input("Enter the Student phy num"))
chemistry=eval(input("Enter the Student chem num "))
Total_marks=maths+physics+chemistry
percentage=(Total_marks/300)*100
print(percentage)
if(percentage<=100 and percentage>=90):
    print("A")
elif(percentage<90 and percentage>=80):
    print("B")
elif(percentage<80 and percentage>=70):
    print("C")
elif(percentage<70 and percentage>=60):
    print("D")
else:
    print("Fail")
    
