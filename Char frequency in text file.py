from os import strerror

#0. Initalizations: creation of a dictionnary to record the characters
char_dict = {}

#1. Open the source file in reading mode

sce_name = input("Enter the name of the text file you wish to use: ")

try:
    sce_file = open(sce_name, 'rt')
    ccount = 0

#2. Read the text file and count the characters
    for ch in sce_file.read():
        if (ch.isalpha()):
            l_ch = ch.lower() #change the letter in lowercase by default 
            if (l_ch in char_dict.keys()):
                #just increment number for that character
                char_dict[l_ch] += 1           
            else:
                #it's a letter but not yet in the dictionnary -> add it
                char_dict[l_ch] = 1
           
    #4. Print the dictionnary
    print(len(char_dict))
    
    for letter, number in sorted(char_dict.items()):
        print(letter, "->", number)
    
    sce_file.close()

except IOError as e:
    print("Cannot open the text file given: ", strerror(e.errno))
    exit(e.errno)


