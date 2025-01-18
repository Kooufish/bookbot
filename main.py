import string 

def main(): 

    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 

        print("--- Begin report of books/frankenstein.txt ---")

        def wordcounter(book):

            count = len(book.split())
            print(f"{count} words found in the document")

        wordcounter(file_contents)

        def charcounter(book):

            uniqeletters = {}
            lettername = ""
            counter = 0
        
            for s in string.ascii_letters.lower():
                

                for letter in book.lower():
                    if letter == s:
                        lettername = s
                        counter += 1

                print(f"the '{lettername}' character was found {counter} times")
                uniqeletters[lettername] = counter
                counter = 0
            
            for letter in book.lower():
                    if letter == " ":
                        lettername = letter
                        counter +=1

            uniqeletters[lettername] = counter 


            

            print("--- End report ---")            

           # print(f"' ': {counter}")
     
        charcounter(file_contents)    

  
main()