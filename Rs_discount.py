rs=int(input("Enter the number of Rs you used: "))
if rs>2000:
  dis=rs*0.20
elif rs>=1000 and  rs<=2000:
  dis=rs*0.10
else:
  dis=0
print(f"Discount: {dis:.2f}")
print(f"Rs after discount: {rs-dis}")
