def print_char(word, i):
    # base condition 
    if i == len(word):
        return

    # action performed
    print(word[i])

    # recursive call
    print_char(word, i+1)


print_char("Aayam", 0)