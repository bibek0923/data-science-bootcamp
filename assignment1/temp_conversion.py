def convert_to_fahrenheit(temp):
    fahr_temp=(temp*9/5)+32
    print("temperature in fahrneit is ",fahr_temp)
    
def main():
    celcius=float(input("enter temp in celcius :"))
    convert_to_fahrenheit(celcius)
    
if __name__ =="__main__":
    main()