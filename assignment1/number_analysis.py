entered_number = int(input("enter a number :"))
print(type(entered_number))
if entered_number % 2==0:
    print("even")
else :
    print("odd")
    

for i in range(1,entered_number+1,1):
    if i%2==0:
        print(i)

sum=0
while(entered_number!=0):
   
    sum = sum + entered_number
    entered_number=entered_number-1
    
print(f"sum is {sum}")
        