import time
import string
def count_lines_words(a):
    # print(a)
    c=0
    d=1
    for letter in a:
        c+=1
        
        if(letter=="\n"):
            d+=1
    print("number of lines is ",d)
    # Splits the text into words using whitespace as the delimiter.
    #this method counts "." also
    # splitted_text= a.split()   
    # print(splitted_text)
    # word_count=len(splitted_text)
    # print(word_count)
    

  #better approach to count numbers
    #a = a.replace('.', '')  . gets replaced and use above method
   
    text =a
    text=text.translate(str.maketrans('','',string.punctuation))
    #  str.maketrans(x, y, z).  x and y are used for mapping characters (used when you want to replace characters).z is used for deleting characters.
    splitted_text=text.split()
    word_count=len(splitted_text)
    print("word count is",  word_count)
    



def main():
    
# file = open("textfile.txt","w")

# # try:
# #     file.write("i am bibek . I am currently learning data science using python")
# # finally:
# #     file.close()

    with open("textfile.txt",'w') as file:
             file.write("I am bibek . \nI live in Kathmandu . \nI am handsome \n hello bro")
    
    with open("textfile.txt",'r') as file:
        a= file.read()
    
        # print(a)
        count_lines_words(a)
        

if __name__=="__main__":
    main()

