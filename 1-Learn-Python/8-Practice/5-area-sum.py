def area_sum(rectangles):
    sum = 0
    for rectangle in rectangles:
        height = rectangle["height"]
        width = rectangle["width"]
        area = height*width
        sum += area

    return sum
    
