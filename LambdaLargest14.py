Largest = lambda X , Y , Z : X if (X > Y and X > Z) else(Y if Y > Z else Z)

No1 = int(input("Enter first number :"))
No2 = int(input("Enter second number :"))
No3 = int(input("Enter third number :"))

Ans = Largest(No1,No2,No3)

print("Largest number is :",Ans)