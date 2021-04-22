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
           
    #3. Order the results from higher to lower number
    # Creation of a new dictionnary with new set order
    # lambda function is passed in key to perform sort by key 
    # passing 2nd element of items()
    # adding "reversed = True" for reversed order
    dic_nborder = {key : val for key, val in sorted(char_dict.items(), key = lambda elem:elem[1], reverse = True)}

    for letter, number in dic_nborder.items():
        print(letter, "->", number)   

except IOError as e:
    print("Cannot open the text file given: ", strerror(e.errno))
    exit(e.errno)

#4. Create a new file to save the histogram
dest_name = str(sce_name + '_histo.txt')
try:
    dest_file = open(dest_name, 'wt')
except Exception as e:
    print("Cannot create destination file: ", strerror(e.errno))
    sce_file.close()
    exit(e.errno)

#5. Write the content of the oredred dictionnary in the new file
try:
    for letter, number in dic_nborder.items():
        dest_file.write(letter + " -> " + str(number)+ "\n")

except IOError as e:
    print("Cannot open the text file given: ", strerror(e.errno))
    exit(e.errno)

sce_file.close()
dest_file.close()

