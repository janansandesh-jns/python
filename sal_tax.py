sal=int(input("Enter your salary: "))
if sal<=300000:
  tax=0
elif sal>300000 and sal<=600000:
  tax=0.05*sal
elif sal>600000 and sal<=1000000:
  tax=0.10*sal
else:
  tax=0.20*sal
print(f"Salary after tax: {sal-tax}")
