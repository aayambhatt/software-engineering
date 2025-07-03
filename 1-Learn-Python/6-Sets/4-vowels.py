def count_vowels(text):
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    unqiue_set = set()

    for i in text:
        if i in vowel_set:
            vowel_count+=1
            unqiue_set.add(i)
    return vowel_count, unqiue_set



    
    
        
