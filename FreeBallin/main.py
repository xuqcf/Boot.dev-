def check_ingredient_match(recipe, inventory):
    has = []
    missing = []

    for ingredient in recipe:
        if ingredient in inventory:
            has.append(ingredient)
        else:
            missing.append(ingredient)
    
    percentage = (len(has) /len(recipe)) * 100

    return percentage, missing

