def safe_divide(a,b):
        try:
            return(a/b)
         
    
    
        except(ZeroDivisionError):
            print(" try remove 0")
def main():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(safe_divide(a,b))
    
if __name__=="__main__":
    main()