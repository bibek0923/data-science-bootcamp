def str_analysis(str):
    count=0
    cons=0
    word=1
    leng = len(str.strip())
    print(leng)
    for letter in str:
        if letter in "aeiouAEIOU":
            count +=1
        elif letter.isalpha():
            cons=cons+1
        else :
            word+=1
    
    print("number of vowel is ",count , "consonant is",cons,"words are",word)



def main():
    str = input("enter a string :")
    str_analysis(str)

if __name__=="__main__":
    main()