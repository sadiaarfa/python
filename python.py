num1= int(input("Enter the first number: "))
operator = input("Enter operator: ")
num2= int(input("Enter the second number: "))
if operator == "+":
    print("Addition of the two numbers is: ",num1+num2)   
elif operator == "-":
    print("Subtraction of the two numbers is: ",num1-num2)
elif operator == "*" or operator == "x":
    print("Multiplication of the two numbers is: ",num1*num2)
elif operator == "/":
    print("Division of the two numbers is: ",num1/num2)
print("\nTo calculate percentage of your obtained marks\n")
total=int(input("Enter total num: "))
Obtained=int(input("Enter the obtain marks: "))
percentage =Obtained*100/total
print("You got",percentage,"% marks")
print("\nTo calculate Marks from percentage of your obtained marks\n")

total2=int(input("Enter the total marks: "))
percentage2=float(input("Enter the percentage of marks: "))
marks = percentage2/100*total2
print("You got total of: ",marks," Marks out of: ",total2)