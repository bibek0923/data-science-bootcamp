def sum(n):
    if(n==0):
        return n
    else :
        return(n+sum(n-1))
a=int(input("enter a number:"))
print(sum(a))