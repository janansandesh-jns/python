y=int(input("How many years have you worked in your company"))
sal=int(input("What is your salary"))
if y>10:
  
  bo=0.10*sal
elif y>=5 and y<=10:

  bo=0.05*sal
else:
 
  bo=0.02*sal
print(f"bonus: {bo} ")
print(f"Salary: {sal}")
print(f"Totally your salary is {sal+bo}")
