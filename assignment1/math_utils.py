def factorial(n):
    fact=1
    if(n==0):
        return(0)
    for i in range (1,n+1):
        fact=fact*i
    return(fact)

def greatest_common_divisor(a,b):
    if(a==0 and b!=0):
        return(b)
    elif(a!=0 and b==0):
        return(a)
    
    elif(a==0 and b ==0):
        return(0)
    
    elif(a<b):
        number = a
    else :
        number =b
    
    
    hcf =1
    for i in range (2,number+1):
        if(a % i==0 and b%i==0):
            hcf =i
    return(hcf)
 
# euclidean algorithm loop   to find hcf        
# def greatest_common_divisor(a, b):
#     while b:
#         a, b = b, a % b
#     return abs(a)


def least_common_multiple(a,b):
   hcf= greatest_common_divisor(a,b)
   lcm=(a*b)/hcf
   return lcm
    

    

    

            
    
    
    