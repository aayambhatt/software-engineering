def join_strings(strings):
    final_string = ""

    for i in range(len(strings)):
        if i ==0:
            final_string+=strings[i]
        else:
            final_string += "," + strings[i]
    
    return final_string 
