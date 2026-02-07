def sum_nested_list(lst):
    total = 0

    for item in lst:
        if isinstance(item, int):
            total += item

        if isinstance(item, list):
            total += sum_nested_list(item)
    
    return total

