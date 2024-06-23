class Person:
    def __init__( self,name,age,email):
        self.username=name
        self.user_age=age
        self.user_email=email
    
    def display_info(self):
        return f"I am {self.username} . I am {self.user_age} years old. My email address is {self.user_email}"
    
def main () :
     p = Person("bibek",16,"bibekpaneru01@gmail.com")
     print(p.display_info())

if __name__=="__main__":
    main()
    