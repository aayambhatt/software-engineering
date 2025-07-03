def subtract(a,b):
    result = a-b
    return result

result = subtract(5,2)
print(f"the subtraction is {result}")

##############################################

def create_introduction(name, age, height, weight):
    first_part = f"your name is {name} and you are {age} years old"
    second_part = f"you are {height} tall and {weight} kg"
    full_intro = first_part + " " +  second_part
    return full_intro
        
result = create_introduction("Aayam", 22, 5.4, 55)
print(result)