user=int(input("enter a number:"))
sum=0
for i in range(1,user+1):
    if i%2==0:
        sum+= i
print("the sum of even numbers from 1 to", user ," is : ",sum)
