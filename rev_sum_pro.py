num=int(input("Enter a number: "))
rev=0
sum=0
pro=1
for i in range(len(str(num))):
  digit=num%10
  sum=sum+digit
  pro=pro*digit
  rev=rev*10+digit
  num=num//10
print(f"Reversed number: {rev}")
print(f"product: {pro}")
print(f"sum: {sum}")
