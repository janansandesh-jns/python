age=int(input("Enter your age: "))
tp=int(input("Enter the ticket price: "))
if age<12:
  dis=0.50*tp
elif age>=60:
  dis=0.40*tp
else:
  dis=0
print(f"Ticket price with discount: {dis}")
