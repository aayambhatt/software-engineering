def check_ingredient_match(recipe, ingredients):
    match_count = 0
    missing_ingredients = []

    for item in recipe:
        if item in ingredients:
            match_count+=1
        else:
            missing_ingredients.append(item)
    percentage = round( (match_count/len(recipe))*100, 2 )
    return percentage, missing_ingredients

            

    